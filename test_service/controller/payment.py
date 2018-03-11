import os


def get_token(order_id):
    return str(order_id) + os.urandom(16)

