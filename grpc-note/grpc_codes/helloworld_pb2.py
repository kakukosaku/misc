# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='helloworld.proto',
  package='helloworld',
  syntax='proto3',
  serialized_options=_b('\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'),
  serialized_pb=_b('\n\x10helloworld.proto\x12\nhelloworld\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\x0bKakuRequest\x12\x0f\n\x07message\x18\x01 \x03(\t\"-\n\x0cKakuResponse\x12\x10\n\x08response\x18\x01 \x03(\t\x12\x0b\n\x03msg\x18\x02 \x01(\x05\x32\x8c\x01\n\x07Greeter\x12>\n\x08SayHello\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x12\x41\n\nKakumethod\x12\x17.helloworld.KakuRequest\x1a\x18.helloworld.KakuResponse\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='helloworld.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='helloworld.HelloRequest.name', index=0,
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
  serialized_start=32,
  serialized_end=60,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='helloworld.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='helloworld.HelloReply.message', index=0,
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
  serialized_start=62,
  serialized_end=91,
)


_KAKUREQUEST = _descriptor.Descriptor(
  name='KakuRequest',
  full_name='helloworld.KakuRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='helloworld.KakuRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=93,
  serialized_end=123,
)


_KAKURESPONSE = _descriptor.Descriptor(
  name='KakuResponse',
  full_name='helloworld.KakuResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='helloworld.KakuResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='helloworld.KakuResponse.msg', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=125,
  serialized_end=170,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
DESCRIPTOR.message_types_by_name['KakuRequest'] = _KAKUREQUEST
DESCRIPTOR.message_types_by_name['KakuResponse'] = _KAKURESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREQUEST,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloRequest)
  ))
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREPLY,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloReply)
  ))
_sym_db.RegisterMessage(HelloReply)

KakuRequest = _reflection.GeneratedProtocolMessageType('KakuRequest', (_message.Message,), dict(
  DESCRIPTOR = _KAKUREQUEST,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.KakuRequest)
  ))
_sym_db.RegisterMessage(KakuRequest)

KakuResponse = _reflection.GeneratedProtocolMessageType('KakuResponse', (_message.Message,), dict(
  DESCRIPTOR = _KAKURESPONSE,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.KakuResponse)
  ))
_sym_db.RegisterMessage(KakuResponse)


DESCRIPTOR._options = None

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='helloworld.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=173,
  serialized_end=313,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='helloworld.Greeter.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Kakumethod',
    full_name='helloworld.Greeter.Kakumethod',
    index=1,
    containing_service=None,
    input_type=_KAKUREQUEST,
    output_type=_KAKURESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
