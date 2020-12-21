# -*- coding: utf-8 -*-
import grpc
import time
import argparse
import asr_api_pb2_grpc
import asr_api_pb2

CHUNK_MILLIS = 100  # send 100ms of file per request

def create_auth_metadata(token):
    return (("authorization", "Bearer {}".format(token)),)

def get_supported_models(stub, metadata):
    empty_rec = asr_api_pb2.Empty()
    response = stub.GetSupportedModelsInfo(empty_rec, metadata=metadata)
    return response


def find_supported_model(model_name, models):
    for model in models:
        if model.name == model_name:
            return model
    return None


def process_file_bytes(file_path, model, millis, sample_rate=8000, enable_automatic_punctuation = True, only_new=True):
    frames_count = int(millis * sample_rate / 1000)
    try:
        model_request = asr_api_pb2.StreamingRecognitionRequest()
        model_request.config.file_name = file_path
        model_request.config.model = model
        model_request.config.enable_automatic_punctuation = enable_automatic_punctuation
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


def streaming_recognize(model_name, file_path, enable_automatic_punctuation, only_new, token):
    cred = grpc.ssl_channel_credentials()
    channel = grpc.secure_channel('stt.3i-vox.ru:443', cred)
    stub = asr_api_pb2_grpc.SttServiceStub(channel)

    metadata = create_auth_metadata(token)
    model_response = get_supported_models(stub, metadata)

    default_model = ""
    model_sample_rate = 8000
    print('Supported models:')
    for model in model_response.models:
        print('-----------------model-----------------')
        print("Model name: " + str(model.name))
        print("Model sample rate: " + str(model.sample_rate_hertz))

        if model.name.find('ru_telephony_') != -1 and model.name.rfind('_v2_8000') != -1:
            default_model = model.name
            model_sample_rate = model.sample_rate_hertz

    found_model = find_supported_model(model_name, model_response.models)
    if not found_model and default_model:
        print("Model with name", model_name, "isn't supported, change it to the default model", default_model)
        model_name = default_model
    else:
        model_sample_rate = found_model.sample_rate_hertz

    print('---------Start file processing---------')
    print('Model name:' + str(model_name) + " sample rate " + str(model_sample_rate))

    responses = stub.StreamingRecognize(process_file_bytes(file_path, model_name, CHUNK_MILLIS, model_sample_rate, enable_automatic_punctuation, only_new), metadata=metadata)

    result_text = ""
    last_message = ""
    for response in responses:
        if len(response.text) != 0:
            print("----------------message----------------")
            if only_new:
                result_text += response.text + " "
            else:
                result_text = response.text
            last_message = response.text
            print_streaming_recognition_responses(response)
    if enable_automatic_punctuation:
        result_text = last_message

    print("result text:", result_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True, help='Model name')
    parser.add_argument('--file', required=True, help='File name')
    parser.add_argument('--only_new', action='store_true', help='Receive only new results')
    parser.add_argument('--token', required=False, help='OAuth access token')
    parser.add_argument('--punctuation', action='store_true', help='Enable automatic punctuation')

    args = parser.parse_args()

    streaming_recognize(args.model, args.file, args.punctuation, args.only_new, args.token)
