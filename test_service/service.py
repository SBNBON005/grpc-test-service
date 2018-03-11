from concurrent import futures
import time
import grpc
import logging

from test_service.generated_interfaces import service_definition_pb2_grpc
from test_service.generated_interfaces import service_definition_pb2
from test_service import controller


class PaymentServer(service_definition_pb2_grpc.PaymentServiceServicer):

    def GetPaymentStatus(self, request, context):
        print(dict(context.invocation_metadata()))
        payment_reference = request.reference
        print(payment_reference)
        return service_definition_pb2.GetPaymentStatusResponse(status='status OK')

    def GetToken(self, request, context):
        logging.info("GetPaymentStatus order_id=%s, payment_amount=%s", request.order_id, request.payment_amount)
        payment_token = controller.payment.get_token(request.order_id)
        response = service_definition_pb2.GetTokenResponse(payment_token=payment_token)
        return response


def serve():
    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    service_definition_pb2_grpc.add_PaymentServiceServicer_to_server(
        PaymentServer(),
        server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print("started ...")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
