import socket

class new_socket:
    def __init__(self):
        self.client_socket = socket.socket()
        self.client_socket.connect(('localhost', 45687))
