# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import proto.vsperf_pb2 as vsperf__pb2


class ControllerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.VsperfInstall = channel.unary_unary(
        '/vsperf.Controller/VsperfInstall',
        request_serializer=vsperf__pb2.HostInfo.SerializeToString,
        response_deserializer=vsperf__pb2.StatusReply.FromString,
        )
    self.UploadConfigFile = channel.stream_unary(
        '/vsperf.Controller/UploadConfigFile',
        request_serializer=vsperf__pb2.ConfFile.SerializeToString,
        response_deserializer=vsperf__pb2.UploadStatus.FromString,
        )
    self.StartTest = channel.unary_unary(
        '/vsperf.Controller/StartTest',
        request_serializer=vsperf__pb2.ControlVsperf.SerializeToString,
        response_deserializer=vsperf__pb2.StatusReply.FromString,
        )
    self.TestStatus = channel.unary_unary(
        '/vsperf.Controller/TestStatus',
        request_serializer=vsperf__pb2.StatusQuery.SerializeToString,
        response_deserializer=vsperf__pb2.StatusReply.FromString,
        )


class ControllerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def VsperfInstall(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadConfigFile(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartTest(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TestStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ControllerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'VsperfInstall': grpc.unary_unary_rpc_method_handler(
          servicer.VsperfInstall,
          request_deserializer=vsperf__pb2.HostInfo.FromString,
          response_serializer=vsperf__pb2.StatusReply.SerializeToString,
      ),
      'UploadConfigFile': grpc.stream_unary_rpc_method_handler(
          servicer.UploadConfigFile,
          request_deserializer=vsperf__pb2.ConfFile.FromString,
          response_serializer=vsperf__pb2.UploadStatus.SerializeToString,
      ),
      'StartTest': grpc.unary_unary_rpc_method_handler(
          servicer.StartTest,
          request_deserializer=vsperf__pb2.ControlVsperf.FromString,
          response_serializer=vsperf__pb2.StatusReply.SerializeToString,
      ),
      'TestStatus': grpc.unary_unary_rpc_method_handler(
          servicer.TestStatus,
          request_deserializer=vsperf__pb2.StatusQuery.FromString,
          response_serializer=vsperf__pb2.StatusReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'vsperf.Controller', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
