# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dc.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x08\x64\x63.proto\":\n\x07Request\x12\r\n\x05genes\x18\x02 \x03(\t\x12\x10\n\x08ontology\x18\x01 \x01(\t\x12\x0e\n\x06growth\x18\x03 \x01(\x08\"3\n\x05Reply\x12\x14\n\x05nodes\x18\x03 \x03(\x0b\x32\x05.Node\x12\x14\n\x05\x65\x64ges\x18\x04 \x03(\x0b\x32\x05.Edge\"_\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02gi\x18\x02 \x01(\x01\x12\r\n\x05state\x18\x03 \x01(\x01\x12\x0f\n\x07neurons\x18\x04 \x03(\x01\x12\x1f\n\ncoordinate\x18\x05 \x01(\x0b\x32\x0b.Coordinate\"\"\n\nCoordinate\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\":\n\x04\x45\x64ge\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0e\n\x06target\x18\x02 \x01(\t\x12\x12\n\nimportance\x18\x03 \x01(\x05\x32%\n\x08\x44\x65\x65pCell\x12\x19\n\x03Run\x12\x08.Request\x1a\x06.Reply\"\x00\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='genes', full_name='Request.genes', index=0,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ontology', full_name='Request.ontology', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='growth', full_name='Request.growth', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=12,
  serialized_end=70,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='Reply.nodes', index=0,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edges', full_name='Reply.edges', index=1,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=123,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Node.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gi', full_name='Node.gi', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='Node.state', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='neurons', full_name='Node.neurons', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coordinate', full_name='Node.coordinate', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=220,
)


_COORDINATE = _descriptor.Descriptor(
  name='Coordinate',
  full_name='Coordinate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Coordinate.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='Coordinate.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=256,
)


_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='Edge.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='Edge.target', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='importance', full_name='Edge.importance', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=316,
)

_REPLY.fields_by_name['nodes'].message_type = _NODE
_REPLY.fields_by_name['edges'].message_type = _EDGE
_NODE.fields_by_name['coordinate'].message_type = _COORDINATE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Coordinate'] = _COORDINATE
DESCRIPTOR.message_types_by_name['Edge'] = _EDGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'dc_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), dict(
  DESCRIPTOR = _REPLY,
  __module__ = 'dc_pb2'
  # @@protoc_insertion_point(class_scope:Reply)
  ))
_sym_db.RegisterMessage(Reply)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
  DESCRIPTOR = _NODE,
  __module__ = 'dc_pb2'
  # @@protoc_insertion_point(class_scope:Node)
  ))
_sym_db.RegisterMessage(Node)

Coordinate = _reflection.GeneratedProtocolMessageType('Coordinate', (_message.Message,), dict(
  DESCRIPTOR = _COORDINATE,
  __module__ = 'dc_pb2'
  # @@protoc_insertion_point(class_scope:Coordinate)
  ))
_sym_db.RegisterMessage(Coordinate)

Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), dict(
  DESCRIPTOR = _EDGE,
  __module__ = 'dc_pb2'
  # @@protoc_insertion_point(class_scope:Edge)
  ))
_sym_db.RegisterMessage(Edge)



_DEEPCELL = _descriptor.ServiceDescriptor(
  name='DeepCell',
  full_name='DeepCell',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=318,
  serialized_end=355,
  methods=[
  _descriptor.MethodDescriptor(
    name='Run',
    full_name='DeepCell.Run',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_REPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEEPCELL)

DESCRIPTOR.services_by_name['DeepCell'] = _DEEPCELL

# @@protoc_insertion_point(module_scope)
