import socket

class new_socket:
    def __init__(self):
        self.new_socket = socket.socket()
        self.new_socket.bind(('localhost', 45687))
