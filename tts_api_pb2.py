# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tts_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tts_api.proto',
  package='vox.tts',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rtts_api.proto\x12\x07vox.tts\"M\n\x11SynthesizeRequest\x12\r\n\x05model\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\r\n\x05speed\x18\x03 \x01(\x02\x12\x0c\n\x04tone\x18\x04 \x01(\x02\"+\n\x12SynthesizeResponse\x12\x15\n\raudio_content\x18\x01 \x01(\x0c\x32L\n\x03TTS\x12\x45\n\nsynthesize\x12\x1a.vox.tts.SynthesizeRequest\x1a\x1b.vox.tts.SynthesizeResponseb\x06proto3'
)




_SYNTHESIZEREQUEST = _descriptor.Descriptor(
  name='SynthesizeRequest',
  full_name='vox.tts.SynthesizeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='vox.tts.SynthesizeRequest.model', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='vox.tts.SynthesizeRequest.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='vox.tts.SynthesizeRequest.speed', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tone', full_name='vox.tts.SynthesizeRequest.tone', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=26,
  serialized_end=103,
)


_SYNTHESIZERESPONSE = _descriptor.Descriptor(
  name='SynthesizeResponse',
  full_name='vox.tts.SynthesizeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio_content', full_name='vox.tts.SynthesizeResponse.audio_content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=105,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['SynthesizeRequest'] = _SYNTHESIZEREQUEST
DESCRIPTOR.message_types_by_name['SynthesizeResponse'] = _SYNTHESIZERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SynthesizeRequest = _reflection.GeneratedProtocolMessageType('SynthesizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESIZEREQUEST,
  '__module__' : 'tts_api_pb2'
  # @@protoc_insertion_point(class_scope:vox.tts.SynthesizeRequest)
  })
_sym_db.RegisterMessage(SynthesizeRequest)

SynthesizeResponse = _reflection.GeneratedProtocolMessageType('SynthesizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESIZERESPONSE,
  '__module__' : 'tts_api_pb2'
  # @@protoc_insertion_point(class_scope:vox.tts.SynthesizeResponse)
  })
_sym_db.RegisterMessage(SynthesizeResponse)



_TTS = _descriptor.ServiceDescriptor(
  name='TTS',
  full_name='vox.tts.TTS',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=150,
  serialized_end=226,
  methods=[
  _descriptor.MethodDescriptor(
    name='synthesize',
    full_name='vox.tts.TTS.synthesize',
    index=0,
    containing_service=None,
    input_type=_SYNTHESIZEREQUEST,
    output_type=_SYNTHESIZERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TTS)

DESCRIPTOR.services_by_name['TTS'] = _TTS

# @@protoc_insertion_point(module_scope)
