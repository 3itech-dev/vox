import grpc
import tts_api_pb2
import tts_api_pb2_grpc

if __name__ == '__main__':
    cred = grpc.ssl_channel_credentials()
    channel = grpc.secure_channel('tts.3i-vox.xyz:443', cred)
    stub = tts_api_pb2_grpc.TTSStub(channel)

    model = "male"
    text = "Для нач+ала работы введите Ваш текст сюда. Подберите подходящий голос и скорость речи. Чтобы добиться наилучшего " \
           "результата поиграйте знаками препинания. Вы можете менять удар+ение знаком плюс, например: зам+ок и з+амок."
    request = tts_api_pb2.SynthesizeRequest(model=model, text=text)

    result = stub.synthesize(request)
    with open("test_tts.wav", 'wb') as f:
        f.write(result.audio_content)
