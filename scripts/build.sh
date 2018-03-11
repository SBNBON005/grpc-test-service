#!/usr/bin/env bash

echo $PWD

python -m grpc_tools.protoc
    \ --proto_path=../protobuffs
    \ --python_out=.
    \ --grpc_python_out=.
    \ ../protobuffs/service_definition.proto