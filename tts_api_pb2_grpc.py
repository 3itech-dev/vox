# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import tts_api_pb2 as tts__api__pb2


class TTSStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.synthesize = channel.unary_unary(
                '/vox.tts.TTS/synthesize',
                request_serializer=tts__api__pb2.SynthesizeRequest.SerializeToString,
                response_deserializer=tts__api__pb2.SynthesizeResponse.FromString,
                )


class TTSServicer(object):
    """Missing associated documentation comment in .proto file."""

    def synthesize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TTSServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'synthesize': grpc.unary_unary_rpc_method_handler(
                    servicer.synthesize,
                    request_deserializer=tts__api__pb2.SynthesizeRequest.FromString,
                    response_serializer=tts__api__pb2.SynthesizeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vox.tts.TTS', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TTS(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def synthesize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vox.tts.TTS/synthesize',
            tts__api__pb2.SynthesizeRequest.SerializeToString,
            tts__api__pb2.SynthesizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
