import grpc
import tts_api_pb2
import tts_api_pb2_grpc
import argparse


def create_auth_metadata(token):
    return (("authorization", "Bearer {}".format(token)),)


def connect():
    options = [
        ('grpc.max_send_message_length', -1),
        ('grpc.max_receive_message_length', -1)
    ]

    cred = grpc.ssl_channel_credentials()
    channel = grpc.secure_channel('tts.3i-vox.ru:443', cred, options=options)
    stub = tts_api_pb2_grpc.TTSStub(channel)
    return stub


def synthesise(args):
    stub = connect()  # create connection
    metadata = create_auth_metadata(args.token)
    result = stub.GetInfo(tts_api_pb2.Empty(), metadata=metadata)  # get server info (available models & parameters)
    print("Available models:", result.models)

    if args.ssml:
        request = tts_api_pb2.SynthesizeRequest(model=args.model, ssml=args.ssml,
                                                loudness=args.loudness,
                                                speed=args.speed,
                                                sample_rate=args.sample_rate,
                                                noise_type=args.noise_type,
                                                noise_strength=args.noise_strength,
                                                noise_strategy=args.noise_strategy,
                                                save=args.save
                                                )
    elif args.text:
        request = tts_api_pb2.SynthesizeRequest(model=args.model, text=args.text,
                                                loudness=args.loudness,
                                                speed=args.speed,
                                                sample_rate=args.sample_rate,
                                                noise_type=args.noise_type,
                                                noise_strength=args.noise_strength,
                                                noise_strategy=args.noise_strategy,
                                                save=args.save
                                                )
    else:
        raise ValueError("Specify text or ssml argument")
    result = stub.Synthesize(request, metadata=metadata)
    with open("test_tts.wav", 'wb') as f:
        f.write(result.audio_content)
    print(result.id)  # if save=true


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', required=False, help='OAuth access token')
    parser.add_argument('--model', required=True, help='Voice name')
    parser.add_argument('--text', required=False, help='Text to synthesise')
    parser.add_argument('--ssml', required=False, help='Ssml-text to synthesise')
    parser.add_argument('--loudness', required=False, type=int, default=1, help='Loudness')
    parser.add_argument('--speed', required=False, type=int, default=1, help='Speed')
    parser.add_argument('--sample_rate', required=False, type=int, default=22050, help='Sample rate of output wav')
    parser.add_argument('--noise_type', required=False, default="29b908de-1f92-4951-8a9e-4b33e576560e", help='Noise name')
    parser.add_argument('--noise_strength', required=False, type=int, default=20, help='Noise strength')
    parser.add_argument('--noise_strategy', required=False, default="absolute", help='Noise type')
    parser.add_argument('--save', required=False, default=False, help='Save result to db')
    args = parser.parse_args()

    synthesise(args)
    print("Done")
