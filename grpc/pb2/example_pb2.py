# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\x12\x06proto_\"\\\n\x03\x46oo\x12\x10\n\x08\x66oo_name\x18\x01 \x01(\t\x12\x0c\n\x04nums\x18\x02 \x03(\x05\x12\x1c\n\x04\x62\x61rs\x18\x03 \x03(\x0b\x32\x0e.proto_.BarMsg\x1a\x17\n\x03\x42\x61r\x12\x10\n\x08\x62\x61r_name\x18\x01 \x01(\t\"\x1e\n\x06\x42\x61rMsg\x12\t\n\x01i\x18\x01 \x01(\x05\x12\t\n\x01j\x18\x02 \x01(\x05\x62\x06proto3')



_FOO = DESCRIPTOR.message_types_by_name['Foo']
_FOO_BAR = _FOO.nested_types_by_name['Bar']
_BARMSG = DESCRIPTOR.message_types_by_name['BarMsg']
Foo = _reflection.GeneratedProtocolMessageType('Foo', (_message.Message,), {

  'Bar' : _reflection.GeneratedProtocolMessageType('Bar', (_message.Message,), {
    'DESCRIPTOR' : _FOO_BAR,
    '__module__' : 'example_pb2'
    # @@protoc_insertion_point(class_scope:proto_.Foo.Bar)
    })
  ,
  'DESCRIPTOR' : _FOO,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:proto_.Foo)
  })
_sym_db.RegisterMessage(Foo)
_sym_db.RegisterMessage(Foo.Bar)

BarMsg = _reflection.GeneratedProtocolMessageType('BarMsg', (_message.Message,), {
  'DESCRIPTOR' : _BARMSG,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:proto_.BarMsg)
  })
_sym_db.RegisterMessage(BarMsg)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FOO._serialized_start=25
  _FOO._serialized_end=117
  _FOO_BAR._serialized_start=94
  _FOO_BAR._serialized_end=117
  _BARMSG._serialized_start=119
  _BARMSG._serialized_end=149
# @@protoc_insertion_point(module_scope)
