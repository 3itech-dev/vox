# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tts_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rtts_api.proto\x12\x07vox.tts\"\xfb\x02\n\x11SynthesizeRequest\x12\r\n\x05model\x18\x01 \x01(\t\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12\x0e\n\x04ssml\x18\x0b \x01(\tH\x00\x12\x12\n\x05speed\x18\x03 \x01(\x02H\x01\x88\x01\x01\x12\x11\n\x04tone\x18\x04 \x01(\x02H\x02\x88\x01\x01\x12\x18\n\x0bsample_rate\x18\x05 \x01(\rH\x03\x88\x01\x01\x12\x15\n\x08loudness\x18\x06 \x01(\x02H\x04\x88\x01\x01\x12\x17\n\nnoise_type\x18\x07 \x01(\tH\x05\x88\x01\x01\x12\x1b\n\x0enoise_strength\x18\x08 \x01(\rH\x06\x88\x01\x01\x12\x1b\n\x0enoise_strategy\x18\t \x01(\tH\x07\x88\x01\x01\x12\x11\n\x04save\x18\n \x01(\x08H\x08\x88\x01\x01\x42\x0b\n\tutteranceB\x08\n\x06_speedB\x07\n\x05_toneB\x0e\n\x0c_sample_rateB\x0b\n\t_loudnessB\r\n\x0b_noise_typeB\x11\n\x0f_noise_strengthB\x11\n\x0f_noise_strategyB\x07\n\x05_save\"7\n\x12SynthesizeResponse\x12\x15\n\raudio_content\x18\x01 \x01(\x0c\x12\n\n\x02id\x18\x02 \x01(\t\"<\n\tModelInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\"\x9f\x01\n\x0bServiceInfo\x12\x0e\n\x06models\x18\x01 \x03(\t\x12\x39\n\x0bmodels_info\x18\x02 \x03(\x0b\x32$.vox.tts.ServiceInfo.ModelsInfoEntry\x1a\x45\n\x0fModelsInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.vox.tts.ModelInfo:\x02\x38\x01\"\x07\n\x05\x45mpty2\xc6\x02\n\x03TTS\x12/\n\x07GetInfo\x12\x0e.vox.tts.Empty\x1a\x14.vox.tts.ServiceInfo\x12\x45\n\nSynthesize\x12\x1a.vox.tts.SynthesizeRequest\x1a\x1b.vox.tts.SynthesizeResponse\x12\x45\n\nsynthesize\x12\x1a.vox.tts.SynthesizeRequest\x1a\x1b.vox.tts.SynthesizeResponse\x12\x30\n\x08get_info\x12\x0e.vox.tts.Empty\x1a\x14.vox.tts.ServiceInfo\x12N\n\x11stream_synthesize\x12\x1a.vox.tts.SynthesizeRequest\x1a\x1b.vox.tts.SynthesizeResponse0\x01\x62\x06proto3')



_SYNTHESIZEREQUEST = DESCRIPTOR.message_types_by_name['SynthesizeRequest']
_SYNTHESIZERESPONSE = DESCRIPTOR.message_types_by_name['SynthesizeResponse']
_MODELINFO = DESCRIPTOR.message_types_by_name['ModelInfo']
_SERVICEINFO = DESCRIPTOR.message_types_by_name['ServiceInfo']
_SERVICEINFO_MODELSINFOENTRY = _SERVICEINFO.nested_types_by_name['ModelsInfoEntry']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
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

ModelInfo = _reflection.GeneratedProtocolMessageType('ModelInfo', (_message.Message,), {
  'DESCRIPTOR' : _MODELINFO,
  '__module__' : 'tts_api_pb2'
  # @@protoc_insertion_point(class_scope:vox.tts.ModelInfo)
  })
_sym_db.RegisterMessage(ModelInfo)

ServiceInfo = _reflection.GeneratedProtocolMessageType('ServiceInfo', (_message.Message,), {

  'ModelsInfoEntry' : _reflection.GeneratedProtocolMessageType('ModelsInfoEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERVICEINFO_MODELSINFOENTRY,
    '__module__' : 'tts_api_pb2'
    # @@protoc_insertion_point(class_scope:vox.tts.ServiceInfo.ModelsInfoEntry)
    })
  ,
  'DESCRIPTOR' : _SERVICEINFO,
  '__module__' : 'tts_api_pb2'
  # @@protoc_insertion_point(class_scope:vox.tts.ServiceInfo)
  })
_sym_db.RegisterMessage(ServiceInfo)
_sym_db.RegisterMessage(ServiceInfo.ModelsInfoEntry)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'tts_api_pb2'
  # @@protoc_insertion_point(class_scope:vox.tts.Empty)
  })
_sym_db.RegisterMessage(Empty)

_TTS = DESCRIPTOR.services_by_name['TTS']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SERVICEINFO_MODELSINFOENTRY._options = None
  _SERVICEINFO_MODELSINFOENTRY._serialized_options = b'8\001'
  _SYNTHESIZEREQUEST._serialized_start=27
  _SYNTHESIZEREQUEST._serialized_end=406
  _SYNTHESIZERESPONSE._serialized_start=408
  _SYNTHESIZERESPONSE._serialized_end=463
  _MODELINFO._serialized_start=465
  _MODELINFO._serialized_end=525
  _SERVICEINFO._serialized_start=528
  _SERVICEINFO._serialized_end=687
  _SERVICEINFO_MODELSINFOENTRY._serialized_start=618
  _SERVICEINFO_MODELSINFOENTRY._serialized_end=687
  _EMPTY._serialized_start=689
  _EMPTY._serialized_end=696
  _TTS._serialized_start=699
  _TTS._serialized_end=1025
# @@protoc_insertion_point(module_scope)
