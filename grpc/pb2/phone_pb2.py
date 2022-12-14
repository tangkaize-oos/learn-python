# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: phone.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bphone.proto\x12\x04main\x1a\x19google/protobuf/any.proto\"f\n\x04User\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1c\n\x07\x63ontent\x18\x03 \x03(\x0b\x32\x0b.main.Phone\x12#\n\x05Value\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\"*\n\x05Phone\x12\x11\n\tphoneType\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\x05\"\x16\n\x06Remark\x12\x0c\n\x04note\x18\x01 \x01(\t*.\n\tPhoneType\x12\r\n\tTelephone\x10\x00\x12\x08\n\x04Home\x10\x01\x12\x08\n\x04Work\x10\x02\x62\x06proto3')

_PHONETYPE = DESCRIPTOR.enum_types_by_name['PhoneType']
PhoneType = enum_type_wrapper.EnumTypeWrapper(_PHONETYPE)
Telephone = 0
Home = 1
Work = 2


_USER = DESCRIPTOR.message_types_by_name['User']
_PHONE = DESCRIPTOR.message_types_by_name['Phone']
_REMARK = DESCRIPTOR.message_types_by_name['Remark']
User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'phone_pb2'
  # @@protoc_insertion_point(class_scope:main.User)
  })
_sym_db.RegisterMessage(User)

Phone = _reflection.GeneratedProtocolMessageType('Phone', (_message.Message,), {
  'DESCRIPTOR' : _PHONE,
  '__module__' : 'phone_pb2'
  # @@protoc_insertion_point(class_scope:main.Phone)
  })
_sym_db.RegisterMessage(Phone)

Remark = _reflection.GeneratedProtocolMessageType('Remark', (_message.Message,), {
  'DESCRIPTOR' : _REMARK,
  '__module__' : 'phone_pb2'
  # @@protoc_insertion_point(class_scope:main.Remark)
  })
_sym_db.RegisterMessage(Remark)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PHONETYPE._serialized_start=220
  _PHONETYPE._serialized_end=266
  _USER._serialized_start=48
  _USER._serialized_end=150
  _PHONE._serialized_start=152
  _PHONE._serialized_end=194
  _REMARK._serialized_start=196
  _REMARK._serialized_end=218
# @@protoc_insertion_point(module_scope)
