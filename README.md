# grpc-test-service
The service I use to experiment on grpc.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
You need docker installed on your machine.

## Bringing service up
Build docker image
```
$ cd /path/to/root/grpc-test-service
$ docker build -t grpc-test-service:dev .
```
Run docker container

```
$ docker run -t --name grpc-test-service grpc-test-service:dev 
```