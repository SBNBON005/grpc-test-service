#!/usr/bin/env bash

echo $PWD

python -m grpc_tools.protoc
    \ --proto_path=protobuffs
    \ --python_out=test_service/generated_interfaces
    \ --grpc_python_out=test_service/generated_interfaces
    \ protobuffs/service_definition.proto