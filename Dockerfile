# Use an official Python runtime as a parent image
FROM python:3.6

MAINTAINER Bongani Sibanda <sibandabongz@gmail.com>

# Set the working directory to /usr/local/test_service
WORKDIR /usr/local/test_service

ENV TZ=Africa/Johannesburg

COPY ./requirements.txt /usr/local/test_service/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt grpcio-tools==1.10.0

ADD . /usr/local/test_service

RUN pip install --upgrade pip && \
    pip install -e .

EXPOSE 50051

CMD test_service