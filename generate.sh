#!/usr/bin/env bash

/usr/bin/python3 -m pip install -U grpcio_tools
/usr/bin/python3 -m grpc_tools.protoc -I ./proto --python_out=. --grpc_python_out=. ./proto/asr_api.proto

