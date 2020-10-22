# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: asr_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='asr_api.proto',
  package='asr',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rasr_api.proto\x12\x03\x61sr\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/api/annotations.proto\",\n\x0eModelsResponse\x12\x1a\n\x06models\x18\x01 \x03(\x0b\x32\n.asr.Model\"0\n\x05Model\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\r\"S\n\x12RecognitionRequest\x12&\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x16.asr.RecognitionConfig\x12\x15\n\raudio_content\x18\x02 \x01(\x0c\"\x87\x01\n\x1bStreamingRecognitionRequest\x12(\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x16.asr.RecognitionConfigH\x00\x12\x17\n\raudio_content\x18\x02 \x01(\x0cH\x00\x12\x10\n\x08only_new\x18\x03 \x01(\x08\x42\x13\n\x11streaming_request\"[\n\x11RecognitionConfig\x12\r\n\x05model\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12$\n\x1c\x65nable_automatic_punctuation\x18\x03 \x01(\x08\"P\n\x13RecognitionResponse\x12+\n\x06\x63hunks\x18\x01 \x03(\x0b\x32\x1b.asr.SpeechRecognitionChunk\x12\x0c\n\x04text\x18\x02 \x01(\t\"|\n\x1cStreamingRecognitionResponse\x12+\n\x06\x63hunks\x18\x01 \x03(\x0b\x32\x1b.asr.SpeechRecognitionChunk\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\r\n\x05\x66inal\x18\x04 \x01(\x08\"\xd0\x01\n\x16SpeechRecognitionChunk\x12-\n\nstart_time\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12+\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\r\n\x05words\x18\x03 \x03(\t\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x12\x10\n\x08loudness\x18\x05 \x01(\x02\x12\x12\n\nspeaker_id\x18\x06 \x01(\t\x12\x11\n\tphrase_id\x18\x07 \x01(\r\"\x07\n\x05\x45mpty2\x84\x02\n\nSttService\x12\x39\n\x16GetSupportedModelsInfo\x12\n.asr.Empty\x1a\x13.asr.ModelsResponse\x12\\\n\tRecognize\x12\x17.asr.RecognitionRequest\x1a\x18.asr.RecognitionResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v1/stt:recognize:\x01*\x12]\n\x12StreamingRecognize\x12 .asr.StreamingRecognitionRequest\x1a!.asr.StreamingRecognitionResponse(\x01\x30\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_MODELSRESPONSE = _descriptor.Descriptor(
  name='ModelsResponse',
  full_name='asr.ModelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='models', full_name='asr.ModelsResponse.models', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=84,
  serialized_end=128,
)


_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='asr.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='asr.Model.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_rate_hertz', full_name='asr.Model.sample_rate_hertz', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=130,
  serialized_end=178,
)


_RECOGNITIONREQUEST = _descriptor.Descriptor(
  name='RecognitionRequest',
  full_name='asr.RecognitionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='asr.RecognitionRequest.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_content', full_name='asr.RecognitionRequest.audio_content', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
  serialized_start=180,
  serialized_end=263,
)


_STREAMINGRECOGNITIONREQUEST = _descriptor.Descriptor(
  name='StreamingRecognitionRequest',
  full_name='asr.StreamingRecognitionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='asr.StreamingRecognitionRequest.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_content', full_name='asr.StreamingRecognitionRequest.audio_content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='only_new', full_name='asr.StreamingRecognitionRequest.only_new', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
    _descriptor.OneofDescriptor(
      name='streaming_request', full_name='asr.StreamingRecognitionRequest.streaming_request',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=266,
  serialized_end=401,
)


_RECOGNITIONCONFIG = _descriptor.Descriptor(
  name='RecognitionConfig',
  full_name='asr.RecognitionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='asr.RecognitionConfig.model', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='asr.RecognitionConfig.file_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_automatic_punctuation', full_name='asr.RecognitionConfig.enable_automatic_punctuation', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=403,
  serialized_end=494,
)


_RECOGNITIONRESPONSE = _descriptor.Descriptor(
  name='RecognitionResponse',
  full_name='asr.RecognitionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunks', full_name='asr.RecognitionResponse.chunks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='asr.RecognitionResponse.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=496,
  serialized_end=576,
)


_STREAMINGRECOGNITIONRESPONSE = _descriptor.Descriptor(
  name='StreamingRecognitionResponse',
  full_name='asr.StreamingRecognitionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunks', full_name='asr.StreamingRecognitionResponse.chunks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='asr.StreamingRecognitionResponse.session_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='asr.StreamingRecognitionResponse.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='final', full_name='asr.StreamingRecognitionResponse.final', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=578,
  serialized_end=702,
)


_SPEECHRECOGNITIONCHUNK = _descriptor.Descriptor(
  name='SpeechRecognitionChunk',
  full_name='asr.SpeechRecognitionChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='asr.SpeechRecognitionChunk.start_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='asr.SpeechRecognitionChunk.end_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='words', full_name='asr.SpeechRecognitionChunk.words', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='asr.SpeechRecognitionChunk.confidence', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loudness', full_name='asr.SpeechRecognitionChunk.loudness', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speaker_id', full_name='asr.SpeechRecognitionChunk.speaker_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phrase_id', full_name='asr.SpeechRecognitionChunk.phrase_id', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=705,
  serialized_end=913,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='asr.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=915,
  serialized_end=922,
)

_MODELSRESPONSE.fields_by_name['models'].message_type = _MODEL
_RECOGNITIONREQUEST.fields_by_name['config'].message_type = _RECOGNITIONCONFIG
_STREAMINGRECOGNITIONREQUEST.fields_by_name['config'].message_type = _RECOGNITIONCONFIG
_STREAMINGRECOGNITIONREQUEST.oneofs_by_name['streaming_request'].fields.append(
  _STREAMINGRECOGNITIONREQUEST.fields_by_name['config'])
_STREAMINGRECOGNITIONREQUEST.fields_by_name['config'].containing_oneof = _STREAMINGRECOGNITIONREQUEST.oneofs_by_name['streaming_request']
_STREAMINGRECOGNITIONREQUEST.oneofs_by_name['streaming_request'].fields.append(
  _STREAMINGRECOGNITIONREQUEST.fields_by_name['audio_content'])
_STREAMINGRECOGNITIONREQUEST.fields_by_name['audio_content'].containing_oneof = _STREAMINGRECOGNITIONREQUEST.oneofs_by_name['streaming_request']
_RECOGNITIONRESPONSE.fields_by_name['chunks'].message_type = _SPEECHRECOGNITIONCHUNK
_STREAMINGRECOGNITIONRESPONSE.fields_by_name['chunks'].message_type = _SPEECHRECOGNITIONCHUNK
_SPEECHRECOGNITIONCHUNK.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_SPEECHRECOGNITIONCHUNK.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['ModelsResponse'] = _MODELSRESPONSE
DESCRIPTOR.message_types_by_name['Model'] = _MODEL
DESCRIPTOR.message_types_by_name['RecognitionRequest'] = _RECOGNITIONREQUEST
DESCRIPTOR.message_types_by_name['StreamingRecognitionRequest'] = _STREAMINGRECOGNITIONREQUEST
DESCRIPTOR.message_types_by_name['RecognitionConfig'] = _RECOGNITIONCONFIG
DESCRIPTOR.message_types_by_name['RecognitionResponse'] = _RECOGNITIONRESPONSE
DESCRIPTOR.message_types_by_name['StreamingRecognitionResponse'] = _STREAMINGRECOGNITIONRESPONSE
DESCRIPTOR.message_types_by_name['SpeechRecognitionChunk'] = _SPEECHRECOGNITIONCHUNK
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelsResponse = _reflection.GeneratedProtocolMessageType('ModelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODELSRESPONSE,
  '__module__' : 'asr_api_pb2'
  # @@protoc_insertion_point(class_scope:asr.ModelsResponse)
  })
_sym_db.RegisterMessage(ModelsResponse)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {
  'DESCRIPTOR' : _MODEL,
  '__module__' : 'asr_api_pb2'
  # @@protoc_insertion_point(class_scope:asr.Model)
  })
_sym_db.RegisterMessage(Model)

RecognitionRequest = _reflection.GeneratedProtocolMessageType('RecognitionRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONREQUEST,
  '__module__' : 'asr_api_pb2'
  # @@protoc_insertion_point(class_scope:asr.RecognitionRequest)
  })
_sym_db.RegisterMessage(RecognitionRequest)

StreamingRecognitionRequest = _reflection.GeneratedProtocolMessageType('StreamingRecognitionRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNITIONREQUEST,
  '__module__' : 'asr_api_pb2'
  # @@protoc_insertion_point(class_scope:asr.StreamingRecognitionRequest)
  })
_sym_db.RegisterMessage(StreamingRecognitionRequest)

RecognitionConfig = _reflection.GeneratedProtocolMessageType('RecognitionConfig', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONCONFIG,
  '__module__' : 'asr_api_pb2'
  # @@protoc_insertion_point(class_scope:asr.RecognitionConfig)
  })
_sym_db.RegisterMessage(RecognitionConfig)

RecognitionResponse = _reflection.GeneratedProtocolMessageType('RecognitionResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONRESPONSE,
  '__module__' : 'asr_api_pb2'
  # @@protoc_insertion_point(class_scope:asr.RecognitionResponse)
  })
_sym_db.RegisterMessage(RecognitionResponse)

StreamingRecognitionResponse = _reflection.GeneratedProtocolMessageType('StreamingRecognitionResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNITIONRESPONSE,
  '__module__' : 'asr_api_pb2'
  # @@protoc_insertion_point(class_scope:asr.StreamingRecognitionResponse)
  })
_sym_db.RegisterMessage(StreamingRecognitionResponse)

SpeechRecognitionChunk = _reflection.GeneratedProtocolMessageType('SpeechRecognitionChunk', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHRECOGNITIONCHUNK,
  '__module__' : 'asr_api_pb2'
  # @@protoc_insertion_point(class_scope:asr.SpeechRecognitionChunk)
  })
_sym_db.RegisterMessage(SpeechRecognitionChunk)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'asr_api_pb2'
  # @@protoc_insertion_point(class_scope:asr.Empty)
  })
_sym_db.RegisterMessage(Empty)



_STTSERVICE = _descriptor.ServiceDescriptor(
  name='SttService',
  full_name='asr.SttService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=925,
  serialized_end=1185,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSupportedModelsInfo',
    full_name='asr.SttService.GetSupportedModelsInfo',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_MODELSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Recognize',
    full_name='asr.SttService.Recognize',
    index=1,
    containing_service=None,
    input_type=_RECOGNITIONREQUEST,
    output_type=_RECOGNITIONRESPONSE,
    serialized_options=b'\202\323\344\223\002\026\"\021/v1/stt:recognize:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamingRecognize',
    full_name='asr.SttService.StreamingRecognize',
    index=2,
    containing_service=None,
    input_type=_STREAMINGRECOGNITIONREQUEST,
    output_type=_STREAMINGRECOGNITIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STTSERVICE)

DESCRIPTOR.services_by_name['SttService'] = _STTSERVICE

# @@protoc_insertion_point(module_scope)