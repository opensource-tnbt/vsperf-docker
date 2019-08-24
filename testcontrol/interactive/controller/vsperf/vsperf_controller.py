# Copyright 2018-19 Spirent Communications.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=R0904
# pylint: disable=R0902
# twenty-two is reasonable in this script

"""
VSPER docker-controller.
"""

import io
import time
import ast
import math

from concurrent import futures

import grpc
from proto import vsperf_pb2
from proto import vsperf_pb2_grpc
from utils import ssh

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


# pylint: disable=too-few-public-methods,no-self-use
class PseudoFile(io.RawIOBase):
    """
    Handle ssh command output.
    """

    def write(self, chunk):
        """
        Write to file
        """
        if "error" in chunk:
            return
        with open("./output.txt", "w") as fref:
            fref.write(chunk)


class VsperfController(vsperf_pb2_grpc.ControllerServicer):
    """
    Main Controller Class
    """

    def __init__(self):
        """
        Initialization
        """
        self.client = None
        self.dut = None
        self.user = None
        self.pwd = None
        self.vsperf_conf = None
        self.tgen_client = None
        self.tgen = None
        self.tgen_user = None
        self.tgenpwd = None
        self.tgen_conf = None
        self.scenario = None
        self.testcase = None
        self.tgen_ip_address = None
        self.testtype = None
        self.trex_conf = None
        self.trex_params = None
        self.conffile = None
        # Default TGen is T-Rex
        self.trex_conffile = "trex_cfg.yml"
        self.collectd_conffile = "collectd.conf"

    def setup(self):
        """
        Performs Setup of the client.
        """
        # Just connect to VM.
        self.client = ssh.SSH(host=self.dut, user=self.user,
                              password=self.pwd)
        self.client.wait()

    def upload_config(self):
        """
        Perform file upload.
        """
        # self.client._put_file_shell(self.conffile, '~/vsperf.conf')
        self.client.put_file(self.conffile, '~/{}'.format(self.conffile))

    def run_test(self):
        """
        Run test
        """
        # Sometimes hugepage store in /mnt/huge in order to free up the
        # hugepage removing this stored hugepage is necessory
        rmv_cmd = "cd /mnt/huge && echo {} | sudo -S rm -rf *".format(self.pwd)
        self.client.run(rmv_cmd, pty=True)
        cmd = "source ~/vsperfenv/bin/activate ; "
        #cmd = "scl enable python33 bash ; "
        cmd += "cd vswitchperf* && "
        cmd += "./vsperf "
        if self.vsperf_conf:
            cmd += "--conf-file ~/{} ".format(self.conffile)
            # cmd += self.conffile
        cmd += self.scenario
        with PseudoFile() as pref:
            self.client.run(cmd, stdout=pref, pty=True, timeout=0)

    def TestStatus(self, request, context):
        """
        Chechk for the test status after performing test
        """
        testtype_list = request.testtype.split(",")
        test_success = []
        test_failed = []
        testtype_list_len = len(testtype_list)
        for test in testtype_list:
            #latest_result_cmd = "find /tmp -mindepth 1 -type d -cmin -5 -printf '%f'"
            test_result_dir = str((self.client.\
                              execute("find /tmp -mindepth 1 -type d -cmin -5 -printf '%f'")[1]).\
                              split('find')[0])
            #test_date_cmd = "date +%F"
            test_date = str(self.client.execute("date +%F")[1]).replace("\n", "")
            if test_date in test_result_dir:
                testcase_check_cmd = "cd /tmp && cd `ls -t | grep results | head -{} | tail -1`".\
                                      format(testtype_list_len)
                testcase_check_cmd += " && find . -maxdepth 1 -name '*{}*'".\
                                        format(test)
                testcase_check_output = str(self.client.execute(testcase_check_cmd)[1]).\
                                        split('\n', 2)
                check = 0
                for i in testcase_check_output:
                    if (".csv" in i) or (".md" in i) or (".rst" in i):
                        check += 1
                if check == 3:
                    test_success.append(test)
                else:
                    test_failed.append(test)
                testtype_list_len -= 1
        if len(testtype_list) == len(test_success):
            return vsperf_pb2.StatusReply(message="All Test Successfully Completed on DUT-Host" \
                                          "Results... [OK]")
        if not test_success:
            return vsperf_pb2.StatusReply(
                message="All Test Failed on DUT-Host \nResults... [Failed]")
        return vsperf_pb2.StatusReply(message="Only {} Test failed   Results ... [Failed]\n"\
                "All other Test Successfully Completed on DUT-Host     Results... [OK] ".\
                format(test_failed))

    def HostConnect(self, request, context):
        """
        Handle host connectivity command from client
        """
        self.dut = request.ip
        self.user = request.uname
        self.pwd = request.pwd
        self.setup()
        return vsperf_pb2.StatusReply(message="Successfully Connected")

    def save_chunks_to_file(self, chunks, filename):
        """
        Write the output to file
        """
        with open(filename, 'w+') as fref:
            fref.write(chunks)

    def UploadConfigFile(self, request, context):
        """
        Handle upload config-file command from client
        """
        chunks = request.Content
        filename = request.Filename
        self.conffile = filename
        self.save_chunks_to_file(chunks, filename)
        # This is chechking if vsperf.conf already exist first remove that and
        # then upload the new file.
        check_test_config_cmd = "find ~/ -maxdepth 1 -name {}".format(filename)
        check_test_result = str(self.client.execute(check_test_config_cmd)[1])
        if "vsperf.conf" in check_test_result:
            self.client.run("rm -f {}".format(filename))
        self.upload_config()
        return vsperf_pb2.UploadStatus(Message="Successfully Uploaded", Code=1)

    def StartTest(self, request, context):
        """
        Handle start-test command from client
        """
        self.vsperf_conf = request.conffile
        self.testtype = request.testtype
        testtype_list = self.testtype.split(",")
        for test in testtype_list:
            self.scenario = test
            self.run_test()
        return vsperf_pb2.StatusReply(message="Test Successfully running...")

###### Traffic Generator Related functions ####
    def TGenHostConnect(self, request, context):
        """
        Connect to TGen-Node
        """
        self.tgen = request.ip
        self.tgen_user = request.uname
        self.tgenpwd = request.pwd
        self.tgen_setup()
        return vsperf_pb2.StatusReply(message="Successfully Connected")

    def tgen_setup(self):
        """
        Setup the T-Gen Client
        """
        # Just connect to VM.
        self.tgen_client = ssh.SSH(host=self.tgen, user=self.tgen_user,
                                   password=self.tgenpwd)
        self.tgen_client.wait()

    def StartBeats(self, request, context):
        """
        Start fileBeats on DUT
        """
        run_cmd = "echo '{}' | sudo -S service filebeat start".format(self.pwd)
        #run_cmd = "sudo service filebeat start"
        self.client.run(run_cmd, pty=True)
        return vsperf_pb2.StatusReply(message="Beats are started on DUT-Host")

    def DUTvsperfTestAvailability(self, request, context):
        """
        Before running test we have to make sure there is no other test running
        """
        vsperf_ava_cmd = "ps -ef | grep -v grep | grep ./vsperf | awk '{print $2}'"
        vsperf_ava_result = len((self.client.execute(vsperf_ava_cmd)[1]).split("\n"))
        if vsperf_ava_result == 1:
            return vsperf_pb2.StatusReply(message="DUT-Host is available for performing \
                                                   VSPERF Test\nYou can perform Test!")
        return vsperf_pb2.StatusReply(message="DUT-Host is busy right now, Wait for some time\n\
            Always Check availability before Running Test!")


###Clean-UP process related functions####


    def vsperf_remove(self):
        """
        Actual removal of the VSPERF
        """
        vsperf_rm_cmd = "echo '{}' | sudo -S rm -r ~/vswitchperf".format(
            self.pwd)
        self.client.run(vsperf_rm_cmd)
        vsperfenv_rm_cmd = "echo '{}' | sudo -S rm -r -f ~/vsperfenv".format(
            self.pwd)
        self.client.run(vsperfenv_rm_cmd)

    def remove_uploaded_config(self):
        """
        Remove all the uploaded configuration files
        """
        vconfig_rm_cmd = "rm ~/vsperf.conf"
        self.client.run(vconfig_rm_cmd)
        tconfig_rm_cmd = "rm /etc/trex_cfg.yml"
        self.tgen_client.run(tconfig_rm_cmd)
        cdconfig_rm_cmd = "echo '{}' | sudo -S rm /opt/collectd/etc/collectd.conf".format(
            self.pwd)
        self.client.run(cdconfig_rm_cmd)

    def result_folder_remove(self):
        """
        Remove result folder on DUT
        """
        remove_cmd = "rm -r /tmp/*results*"
        self.client.run(remove_cmd)

    def collectd_remove(self):
        """
        Remove collectd from DUT
        """
        collectd_dwn_rm_cmd = "echo '{}' | sudo -S rm -r -f ~/collectd".format(
            self.pwd)
        self.client.run(collectd_dwn_rm_cmd)
        collectd_rm_cmd = "echo '{}' | sudo -S rm -r -f /opt/collectd".format(
            self.pwd)
        self.client.run(collectd_rm_cmd)

    def RemoveVsperf(self, request, context):
        """
        Handle VSPERF removal command from client
        """
        self.vsperf_remove()
        return vsperf_pb2.StatusReply(message="Successfully VSPERF Removed")

    def TerminateVsperf(self, request, context):
        """
        Terminate the VSPERF and kill processes
        """
        stress_kill_cmd = "echo '{}' | sudo -S pkill stress &> /dev/null".format(
            self.pwd)
        python3_kill_cmd = "echo '{}' | sudo -S pkill python3 &> /dev/null".format(
            self.pwd)
        qemu_kill_cmd = "echo '{}' | sudo -S killall -9 qemu-system-x86_64 &> /dev/null".format(
            self.pwd)
        self.client.run(stress_kill_cmd)
        self.client.run(python3_kill_cmd)
        self.client.run(qemu_kill_cmd)

        # sometimes qemu resists to terminate, so wait a bit and kill it again
        qemu_check_cmd = "pgrep qemu-system-x86_64"
        qemu_cmd_response = self.client.execute(qemu_check_cmd)[1]

        if qemu_cmd_response != '':
            time.sleep(5)
            self.client.run(qemu_kill_cmd)
            time.sleep(5)

        ovs_kill_cmd = "echo '{}' | sudo pkill ovs-vswitchd &> /dev/null".format(
            self.pwd)
        ovsdb_kill_cmd = "echo '{}' | sudo pkill ovsdb-server &> /dev/null".format(
            self.pwd)
        vppctl_kill_cmd = "echo '{}' | sudo pkill vppctl &> /dev/null".format(
            self.pwd)
        vpp_kill_cmd = "echo '{}' | sudo pkill vpp &> /dev/null".format(
            self.pwd)
        vpp_cmd = "echo '{}' | sudo pkill -9 vpp &> /dev/null".format(self.pwd)

        self.client.run(ovs_kill_cmd)
        time.sleep(1)
        self.client.run(ovsdb_kill_cmd)
        time.sleep(1)
        self.client.run(vppctl_kill_cmd)
        time.sleep(1)
        self.client.run(vpp_kill_cmd)
        time.sleep(1)
        self.client.run(vpp_cmd)
        time.sleep(1)

        return vsperf_pb2.StatusReply(
            message="All the VSPERF related process terminated successfully")

    def RemoveResultFolder(self, request, context):
        """
        Handle result folder removal command from client
        """
        self.result_folder_remove()
        return vsperf_pb2.StatusReply(
            message="Successfully VSPERF Results Removed")

    def RemoveUploadedConfig(self, request, context):
        """
        Handle all configuration file removal command from client
        """
        self.remove_uploaded_config()
        return vsperf_pb2.StatusReply(
            message="Successfully All Uploaded Config Files Removed")

    def RemoveCollectd(self, request, context):
        """
        Handle collectd removal command from client
        """
        self.collectd_remove()
        return vsperf_pb2.StatusReply(
            message="Successfully Collectd Removed From DUT-Host")

    def RemoveEverything(self, request, context):
        """
        Handle of removing everything from DUT command from client
        """
        self.vsperf_remove()
        self.result_folder_remove()
        self.remove_uploaded_config()
        self.collectd_remove()
        return vsperf_pb2.StatusReply(
            message="Successfully Everything Removed From DUT-Host")

    def StartTGen(self, request, context):
        """
        Handle start-Tgen command from client
        """
        self.trex_conf = request.conffile
        self.trex_params = request.params
        run_cmd = "cd trex_2.37/scripts ; "
        run_cmd += "./t-rex-64 "
        run_cmd += self.trex_params
        self.tgen_client.send_command(run_cmd)
        return vsperf_pb2.StatusReply(message="T-Rex Successfully running...")

    def SanityCollectdCheck(self, request, context):
        """
        Check and verify collectd is able to run and start properly
        """
        check_collectd_cmd = "find /opt -maxdepth 1 -name 'collectd'"
        check_test_result = str(self.client.execute(check_collectd_cmd)[1])
        if "collectd" in check_test_result:
            check_collectd_run_cmd = "echo {} | sudo -S service collectd start".format(self.pwd)
            self.client.run(check_collectd_run_cmd, pty=True)
            check_collectd_status_cmd = "ps aux | grep collectd"
            check_collectd_status = str(self.client.execute(check_collectd_status_cmd)[1])
            if "/sbin/collectd" in check_collectd_status:
                return vsperf_pb2.StatusReply(message="Collectd is working Fine")
            return vsperf_pb2.StatusReply(message="Collectd Fail to Start, \
                                                   Install correctly before running Test")
        return vsperf_pb2.StatusReply(message="Collectd is not installed yet.")

    def SanityVNFpath(self, request, context):
        """
        Check if VNF image available on the mention path in Test Config File
        """
        # fetch the VNF path we placed in vsperf.conf file
        vsperf_conf_path = 'cat ~/{} | grep "GUEST_IMAGE"'.format(self.conffile)
        vsperf_conf_read = self.client.execute(vsperf_conf_path)[1]
        vnf_image_path = vsperf_conf_read.split("'")[1]
        vnf_path_check_cmd = "find {}".format(vnf_image_path)
        vfn_path_check_result = str(self.client.execute(vnf_path_check_cmd)[1])
        if vnf_image_path in vfn_path_check_result:
            return vsperf_pb2.StatusReply(message="Test Configratuion file has Correct "\
                "VNF path information on DUT-Host.....[OK]")
        return vsperf_pb2.StatusReply(message='Test Configuration file has wrongly placed VNF '\
            'path information \n'\
            'VNF is not available on DUT-Host................................[Failed]\n ')

    def SanityVSPERFCheck(self, request, context):
        """
        We have to make sure that VSPERF install correctly
        """
        vsperf_check_command = "source ~/vsperfenv/bin/activate ; cd vswitchperf* && "
        vsperf_check_command += "./vsperf --help"
        vsperf_check_cmd_result = str(self.client.execute(vsperf_check_command)[1])
        vsperf_verify_list = [
            'usage',
            'positional arguments',
            'optional arguments',
            'test selection options',
            'test behavior options']
        for idx, i in enumerate(vsperf_verify_list, start=1):
            if str(i) in vsperf_check_cmd_result:
                if idx < 5:
                    continue
                elif idx == 5:
                    return vsperf_pb2.StatusReply(
                        message="VSPERF Installed Correctly and Working fine")
            return vsperf_pb2.StatusReply(message="VSPERF Does Not Installed Correctly ," \
                                          "INSTALL IT AGAIN..............[Critical]")
        return vsperf_pb2.StatusReply(message="VSPERF Does Not Installed Correctly ," \
                                      "INSTALL IT AGAIN..............[Critical]")

    def SanityNICCheck(self, request, context):
        """
        Check either NIC PCI ids are Correctly placed or not
        """
        trex_conf_path = "cat /etc/trex_cfg.yaml | grep interfaces"
        trex_conf_read = self.tgen_client.execute(trex_conf_path)[1]
        nic_pid_ids_list = [trex_conf_read.split("\"")[1], trex_conf_read.split("\"")[3]]
        trex_nic_pic_id_cmd = "lspci | egrep -i --color 'network|ethernet'"
        trex_nic_pic_id = str(self.tgen_client.execute(trex_nic_pic_id_cmd)[1]).split('\n')
        acheck = 0
        for k in trex_nic_pic_id:
            for j in nic_pid_ids_list:
                if j in k:
                    acheck += 1
                else:
                    pass
        if acheck == 2:
            return vsperf_pb2.StatusReply(message="Both the NIC PCI Ids are Correctly "\
                "configured on TGen-Host..............")
        return vsperf_pb2.StatusReply(message="You configured NIC PCI Ids Wrong in "\
                "TGen-Host............................[OK]\n")

    def SanityTgenConnDUTCheck(self, request, context):
        """
        We should confirm the DUT connectivity with the Tgen and Traffic Generator is working or not
        """
        self.tgen_ip_address = request.ip
        tgen_connectivity_check_cmd = "ping {} -c 1".format(
            self.tgen_ip_address)
        tgen_connectivity_check_result = int(
            self.client.execute(tgen_connectivity_check_cmd)[0])
        if tgen_connectivity_check_result == 0:
            return vsperf_pb2.StatusReply(
                message="DUT-Host is successfully reachable to Traffic Generator......")
        return vsperf_pb2.StatusReply(message="DUT-Host is unsuccessful to reach the \
                                      Traffic Generator \nMake sure to establish connection \
                                      between DUT-Host and TGen-Host before running Test\
                                       ............... ")

    def variable_from_test_config(self, aparameter):
        """This function can be use to read any configuration paramter from vsperf.conf"""
        read_cmd = 'cat ~/{} | grep "{}"'.format(aparameter, self.conffile)
        read_cmd_output = str(self.client.execute(read_cmd)[1])
        print(read_cmd_output)
        if not read_cmd_output or '#' in read_cmd_output:
            return 0
        return read_cmd_output.split("=")[1].strip()

    def cpumask2coreids(self, mask):
        """conver mask to coreids"""
        intmask = int(mask, 16)
        i = 1
        coreids = []
        while i < intmask:
            if i & intmask:
                coreids.append(str(math.frexp(i)[1]-1))
            i = i << 1
        return coreids

    def cpu_allocation_check(self, list1, list2):
        """compare to cpu_map list"""
        if len(list1) >= len(list2):
            if all(elem in list1  for elem in list2):
                return vsperf_pb2.StatusReply(message="CPU allocation properly done on" \
                    " DUT-Host.................[OK]")
            return vsperf_pb2.StatusReply(message="CPU allocation not done properly on " \
                "DUT-Host............[Failed]")
        return vsperf_pb2.StatusReply(message="CPU allocation not done properly on" \
            " DUT-Host............[Failed]")

    def SanityCPUAllocationCheck(self, request, context):
        """
        check for cpu-allocation on DUT-Host
        """
        read_setting_cmd = "source vsperfenv/bin/activate ; cd vswitchperf* && "
        read_setting_cmd += './vsperf --list-settings'
        default_vsperf_settings = ast.literal_eval(str(self.client.execute(read_setting_cmd)[1]))
        default_cpu_map = default_vsperf_settings["VSWITCH_VHOST_CPU_MAP"]
        default_vswitch_pmd_cpu_mask = str(default_vsperf_settings["VSWITCH_PMD_CPU_MASK"])
        default_vswitch_vhost_cpu_map = [str(x) for x in default_cpu_map]
        vswitch_pmd_cpu_mask = self.variable_from_test_config("VSWITCH_PMD_CPU_MASK")
        vswitch_cpu_map = (self.variable_from_test_config("VSWITCH_VHOST_CPU_MAP"))
        vswitch_vhost_cpu_map = 0

        if vswitch_cpu_map != 0:
            vswitch_vhost_cpu_map = [str(x) for x in  ast.literal_eval(vswitch_cpu_map)]

        if vswitch_pmd_cpu_mask == 0 and vswitch_vhost_cpu_map == 0:
            return vsperf_pb2.StatusReply(message="CPU allocation Check Done,\
                \nNo vswitch_pmd_cpu_mask or vswitch_vhost_cpu_map assign in test config file" \
                "Using Default Settings..[OK]\n")
        if vswitch_pmd_cpu_mask != 0 and vswitch_vhost_cpu_map == 0:
            core_id = self.cpumask2coreids(vswitch_pmd_cpu_mask)
            return self.cpu_allocation_check(default_vswitch_vhost_cpu_map, core_id)
        if vswitch_pmd_cpu_mask == 0 and vswitch_vhost_cpu_map != 0:
            core_id_1 = self.cpumask2coreids(default_vswitch_pmd_cpu_mask)
            return self.cpu_allocation_check(vswitch_vhost_cpu_map, core_id_1)
        core_id_2 = self.cpumask2coreids(vswitch_pmd_cpu_mask)
        return self.cpu_allocation_check(vswitch_vhost_cpu_map, core_id_2)

    def GetVSPERFConffromDUT(self, request, context):
        """
        This will extract the vsperf test configuration from DUT-Host
        """
        read_cmd = "cat ~/{}".format(self.conffile)
        read_cmd_output = str(self.client.execute(read_cmd)[1])
        return vsperf_pb2.StatusReply(message="{}".format(read_cmd_output))


def serve():
    """
    Start servicing the client
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vsperf_pb2_grpc.add_ControllerServicer_to_server(
        VsperfController(), server)
    server.add_insecure_port('[::]:4000')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except (SystemExit, KeyboardInterrupt, MemoryError, RuntimeError):
        server.stop(0)


if __name__ == "__main__":
    serve()