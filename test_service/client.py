import grpc
import logging

from test_service.generated_interfaces import service_definition_pb2_grpc
from test_service.generated_interfaces import service_definition_pb2

host = 'localhost:50051'
channel = grpc.insecure_channel(host)
stub = service_definition_pb2_grpc.PaymentServiceStub(channel)


def get_payment_status(payment_reference):
    try:
        request = service_definition_pb2.GetPaymentStatusRequest(
            reference=payment_reference)
        response = stub.GetPaymentStatus(request, timeout=10)
        if response:
            print("RESPONSE")
            return response.status
    except grpc.RpcError:
        logging.exception("Error getting payment status:")
        raise
