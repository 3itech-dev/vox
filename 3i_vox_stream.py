# -*- coding: utf-8 -*-
import grpc
import time
import argparse
import asr_api_pb2_grpc
import asr_api_pb2

CHUNK_MILLIS = 100  # send 100ms of file per request


def get_supported_models(stub):
    empty_rec = asr_api_pb2.Empty()
    response = stub.GetSupportedModelsInfo(empty_rec)
    return response


def is_model_supported(model_name, models):
    for model in models:
        if model.name == model_name:
            return True
    return False


def process_file_bytes(file_path, model, millis, sample_rate=8000, only_new=True):
    frames_count = int(millis * sample_rate / 1000)
    try:
        model_request = asr_api_pb2.StreamingRecognitionRequest()
        model_request.config.file_name = file_path
        model_request.config.model = model
        yield model_request
        wav_header_num_bytes = 44  # 44 байта - размер wav заголовка
        with open(file_path, 'rb') as f:
            f.read(wav_header_num_bytes)
            for data in iter(lambda: f.read(frames_count * 2), b''):
                request = asr_api_pb2.StreamingRecognitionRequest()
                request.audio_content = data
                request.only_new = only_new

                yield request
                time.sleep(millis / 1000)
    except Exception as e:
        print("Exception in process_file_bytes", e)
        raise


def format_timestamp(timestamp):
    return "{:>02d}:{:>02d}.{:>03d}".format((timestamp.seconds // 60) % 60, timestamp.seconds % 60, timestamp.microseconds // 1000)


def print_streaming_recognition_responses(response):
    print("text:", response.text)
    for chunk in response.chunks:
        print_msg = "[" + format_timestamp(chunk.start_time.ToTimedelta()) + ".." + format_timestamp(chunk.end_time.ToTimedelta()) + "] "
        for alternative in chunk.words:
            print_msg += '"' + alternative + '", '
        print_msg += "phrase_id: " + str(chunk.phrase_id) + ", loudness: " + str(chunk.loudness) + ", confidence: " + str(chunk.confidence)
        print(print_msg)


def streaming_recognize(model_name, sample_rate, file_path, only_new):
    cred = grpc.ssl_channel_credentials()
    channel = grpc.secure_channel('stt.3i-vox.ru:443', cred)
    stub = asr_api_pb2_grpc.SttServiceStub(channel)

    model_response = get_supported_models(stub)

    default_model = ""
    print('Supported models:')
    for model in model_response.models:
        print('-----------------model-----------------')
        print("Model name: " + str(model.name))
        print("Model sample rate: " + str(model.sample_rate_hertz))

        if model.name.find('ru_telephony_') != -1 and model.name.rfind('_v2_8000') != -1:
            default_model = model.name

    if not is_model_supported(model_name, model_response.models) and default_model:
        print("Model with name", model_name, "isn't supported, change it to the default model", default_model)
        model_name = default_model

    print('---------Start file processing---------')
    print('Model name:' + str(model_name))

    responses = stub.StreamingRecognize(process_file_bytes(file_path, model_name, CHUNK_MILLIS, sample_rate, only_new))

    result_text = ""
    for response in responses:
        if len(response.text) != 0:
            print("----------------message----------------")
            if only_new:
                result_text += response.text + " "
            else:
                result_text = response.text
            print_streaming_recognition_responses(response)

    print("result text:", result_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True, help='Model name')
    parser.add_argument('--rate', required=False, default=8000, help='Sample rate')
    parser.add_argument('--file', required=True, help='File name')
    parser.add_argument('--only_new', action='store_true', help='Receive only new results')


    args = parser.parse_args()

    streaming_recognize(args.model, args.rate, args.file, args.only_new)
