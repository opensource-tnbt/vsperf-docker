# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vsperf.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='vsperf.proto',
  package='vsperf',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cvsperf.proto\x12\x06vsperf\"3\n\rControlVsperf\x12\x10\n\x08testtype\x18\x01 \x01(\t\x12\x10\n\x08\x63onffile\x18\x02 \x01(\t\"/\n\x0b\x43ontrolTGen\x12\x0e\n\x06params\x18\x01 \x01(\t\x12\x10\n\x08\x63onffile\x18\x02 \x01(\t\"\x1b\n\x08\x43onfFile\x12\x0f\n\x07\x43ontent\x18\x01 \x01(\x0c\"2\n\x08HostInfo\x12\n\n\x02ip\x18\x01 \x01(\t\x12\r\n\x05uname\x18\x02 \x01(\t\x12\x0b\n\x03pwd\x18\x03 \x01(\t\"F\n\x0bHostVerInfo\x12\n\n\x02ip\x18\x01 \x01(\t\x12\r\n\x05uname\x18\x02 \x01(\t\x12\x0b\n\x03pwd\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\"\x1f\n\x0bStatusQuery\x12\x10\n\x08testtype\x18\x01 \x01(\t\"\x1e\n\x0bStatusReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"G\n\x0cUploadStatus\x12\x0f\n\x07Message\x18\x01 \x01(\t\x12&\n\x04\x43ode\x18\x02 \x01(\x0e\x32\x18.vsperf.UploadStatusCode*3\n\x10UploadStatusCode\x12\x0b\n\x07Unknown\x10\x00\x12\x06\n\x02Ok\x10\x01\x12\n\n\x06\x46\x61iled\x10\x02\x32\x9d\x05\n\nController\x12\x36\n\x0bHostConnect\x12\x10.vsperf.HostInfo\x1a\x13.vsperf.StatusReply\"\x00\x12\x38\n\rVsperfInstall\x12\x10.vsperf.HostInfo\x1a\x13.vsperf.StatusReply\"\x00\x12>\n\x10UploadConfigFile\x12\x10.vsperf.ConfFile\x1a\x14.vsperf.UploadStatus\"\x00(\x01\x12\x39\n\tStartTest\x12\x15.vsperf.ControlVsperf\x1a\x13.vsperf.StatusReply\"\x00\x12\x38\n\nTestStatus\x12\x13.vsperf.StatusQuery\x1a\x13.vsperf.StatusReply\"\x00\x12:\n\x0fTGenHostConnect\x12\x10.vsperf.HostInfo\x1a\x13.vsperf.StatusReply\"\x00\x12\x39\n\x0bTGenInstall\x12\x13.vsperf.HostVerInfo\x1a\x13.vsperf.StatusReply\"\x00\x12\x42\n\x14TGenUploadConfigFile\x12\x10.vsperf.ConfFile\x1a\x14.vsperf.UploadStatus\"\x00(\x01\x12\x37\n\tStartTGen\x12\x13.vsperf.ControlTGen\x1a\x13.vsperf.StatusReply\"\x00\x12\x38\n\nTGenStatus\x12\x13.vsperf.StatusQuery\x1a\x13.vsperf.StatusReply\"\x00\x12:\n\x0f\x43ollectdInstall\x12\x10.vsperf.HostInfo\x1a\x13.vsperf.StatusReply\"\x00\x62\x06proto3')
)

_UPLOADSTATUSCODE = _descriptor.EnumDescriptor(
  name='UploadStatusCode',
  full_name='vsperf.UploadStatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Ok', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failed', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=417,
  serialized_end=468,
)
_sym_db.RegisterEnumDescriptor(_UPLOADSTATUSCODE)

UploadStatusCode = enum_type_wrapper.EnumTypeWrapper(_UPLOADSTATUSCODE)
Unknown = 0
Ok = 1
Failed = 2



_CONTROLVSPERF = _descriptor.Descriptor(
  name='ControlVsperf',
  full_name='vsperf.ControlVsperf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='testtype', full_name='vsperf.ControlVsperf.testtype', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conffile', full_name='vsperf.ControlVsperf.conffile', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=75,
)


_CONTROLTGEN = _descriptor.Descriptor(
  name='ControlTGen',
  full_name='vsperf.ControlTGen',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='vsperf.ControlTGen.params', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conffile', full_name='vsperf.ControlTGen.conffile', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=124,
)


_CONFFILE = _descriptor.Descriptor(
  name='ConfFile',
  full_name='vsperf.ConfFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Content', full_name='vsperf.ConfFile.Content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=153,
)


_HOSTINFO = _descriptor.Descriptor(
  name='HostInfo',
  full_name='vsperf.HostInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='vsperf.HostInfo.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uname', full_name='vsperf.HostInfo.uname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pwd', full_name='vsperf.HostInfo.pwd', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=205,
)


_HOSTVERINFO = _descriptor.Descriptor(
  name='HostVerInfo',
  full_name='vsperf.HostVerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='vsperf.HostVerInfo.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uname', full_name='vsperf.HostVerInfo.uname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pwd', full_name='vsperf.HostVerInfo.pwd', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='vsperf.HostVerInfo.version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=277,
)


_STATUSQUERY = _descriptor.Descriptor(
  name='StatusQuery',
  full_name='vsperf.StatusQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='testtype', full_name='vsperf.StatusQuery.testtype', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=279,
  serialized_end=310,
)


_STATUSREPLY = _descriptor.Descriptor(
  name='StatusReply',
  full_name='vsperf.StatusReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='vsperf.StatusReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=342,
)


_UPLOADSTATUS = _descriptor.Descriptor(
  name='UploadStatus',
  full_name='vsperf.UploadStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Message', full_name='vsperf.UploadStatus.Message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Code', full_name='vsperf.UploadStatus.Code', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=415,
)

_UPLOADSTATUS.fields_by_name['Code'].enum_type = _UPLOADSTATUSCODE
DESCRIPTOR.message_types_by_name['ControlVsperf'] = _CONTROLVSPERF
DESCRIPTOR.message_types_by_name['ControlTGen'] = _CONTROLTGEN
DESCRIPTOR.message_types_by_name['ConfFile'] = _CONFFILE
DESCRIPTOR.message_types_by_name['HostInfo'] = _HOSTINFO
DESCRIPTOR.message_types_by_name['HostVerInfo'] = _HOSTVERINFO
DESCRIPTOR.message_types_by_name['StatusQuery'] = _STATUSQUERY
DESCRIPTOR.message_types_by_name['StatusReply'] = _STATUSREPLY
DESCRIPTOR.message_types_by_name['UploadStatus'] = _UPLOADSTATUS
DESCRIPTOR.enum_types_by_name['UploadStatusCode'] = _UPLOADSTATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ControlVsperf = _reflection.GeneratedProtocolMessageType('ControlVsperf', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLVSPERF,
  __module__ = 'vsperf_pb2'
  # @@protoc_insertion_point(class_scope:vsperf.ControlVsperf)
  ))
_sym_db.RegisterMessage(ControlVsperf)

ControlTGen = _reflection.GeneratedProtocolMessageType('ControlTGen', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLTGEN,
  __module__ = 'vsperf_pb2'
  # @@protoc_insertion_point(class_scope:vsperf.ControlTGen)
  ))
_sym_db.RegisterMessage(ControlTGen)

ConfFile = _reflection.GeneratedProtocolMessageType('ConfFile', (_message.Message,), dict(
  DESCRIPTOR = _CONFFILE,
  __module__ = 'vsperf_pb2'
  # @@protoc_insertion_point(class_scope:vsperf.ConfFile)
  ))
_sym_db.RegisterMessage(ConfFile)

HostInfo = _reflection.GeneratedProtocolMessageType('HostInfo', (_message.Message,), dict(
  DESCRIPTOR = _HOSTINFO,
  __module__ = 'vsperf_pb2'
  # @@protoc_insertion_point(class_scope:vsperf.HostInfo)
  ))
_sym_db.RegisterMessage(HostInfo)

HostVerInfo = _reflection.GeneratedProtocolMessageType('HostVerInfo', (_message.Message,), dict(
  DESCRIPTOR = _HOSTVERINFO,
  __module__ = 'vsperf_pb2'
  # @@protoc_insertion_point(class_scope:vsperf.HostVerInfo)
  ))
_sym_db.RegisterMessage(HostVerInfo)

StatusQuery = _reflection.GeneratedProtocolMessageType('StatusQuery', (_message.Message,), dict(
  DESCRIPTOR = _STATUSQUERY,
  __module__ = 'vsperf_pb2'
  # @@protoc_insertion_point(class_scope:vsperf.StatusQuery)
  ))
_sym_db.RegisterMessage(StatusQuery)

StatusReply = _reflection.GeneratedProtocolMessageType('StatusReply', (_message.Message,), dict(
  DESCRIPTOR = _STATUSREPLY,
  __module__ = 'vsperf_pb2'
  # @@protoc_insertion_point(class_scope:vsperf.StatusReply)
  ))
_sym_db.RegisterMessage(StatusReply)

UploadStatus = _reflection.GeneratedProtocolMessageType('UploadStatus', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADSTATUS,
  __module__ = 'vsperf_pb2'
  # @@protoc_insertion_point(class_scope:vsperf.UploadStatus)
  ))
_sym_db.RegisterMessage(UploadStatus)



_CONTROLLER = _descriptor.ServiceDescriptor(
  name='Controller',
  full_name='vsperf.Controller',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=471,
  serialized_end=1140,
  methods=[
  _descriptor.MethodDescriptor(
    name='HostConnect',
    full_name='vsperf.Controller.HostConnect',
    index=0,
    containing_service=None,
    input_type=_HOSTINFO,
    output_type=_STATUSREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='VsperfInstall',
    full_name='vsperf.Controller.VsperfInstall',
    index=1,
    containing_service=None,
    input_type=_HOSTINFO,
    output_type=_STATUSREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UploadConfigFile',
    full_name='vsperf.Controller.UploadConfigFile',
    index=2,
    containing_service=None,
    input_type=_CONFFILE,
    output_type=_UPLOADSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartTest',
    full_name='vsperf.Controller.StartTest',
    index=3,
    containing_service=None,
    input_type=_CONTROLVSPERF,
    output_type=_STATUSREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TestStatus',
    full_name='vsperf.Controller.TestStatus',
    index=4,
    containing_service=None,
    input_type=_STATUSQUERY,
    output_type=_STATUSREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TGenHostConnect',
    full_name='vsperf.Controller.TGenHostConnect',
    index=5,
    containing_service=None,
    input_type=_HOSTINFO,
    output_type=_STATUSREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TGenInstall',
    full_name='vsperf.Controller.TGenInstall',
    index=6,
    containing_service=None,
    input_type=_HOSTVERINFO,
    output_type=_STATUSREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TGenUploadConfigFile',
    full_name='vsperf.Controller.TGenUploadConfigFile',
    index=7,
    containing_service=None,
    input_type=_CONFFILE,
    output_type=_UPLOADSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartTGen',
    full_name='vsperf.Controller.StartTGen',
    index=8,
    containing_service=None,
    input_type=_CONTROLTGEN,
    output_type=_STATUSREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TGenStatus',
    full_name='vsperf.Controller.TGenStatus',
    index=9,
    containing_service=None,
    input_type=_STATUSQUERY,
    output_type=_STATUSREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CollectdInstall',
    full_name='vsperf.Controller.CollectdInstall',
    index=10,
    containing_service=None,
    input_type=_HOSTINFO,
    output_type=_STATUSREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROLLER)

DESCRIPTOR.services_by_name['Controller'] = _CONTROLLER

# @@protoc_insertion_point(module_scope)
