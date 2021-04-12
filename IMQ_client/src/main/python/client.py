from client_socket import new_socket
from publisher import Publisher
from subscriber import Subscriber
from protocol import response_protocol
from exceptions.connection_exception import *

try:
    server_socket = new_socket()
except Exception as e:
    raise unableToConnect

class client:
    def __init__(self):
        self.message = input("Enter P for PUBLISHER and S for SUBSCRIBER: ")
        if (self.message.lower() == 'p'):
            server_socket.client_socket.send(bytes(self.message, 'utf-8'))
            print("You are a Publisher")
            Publisher(server_socket)
        elif (self.message.lower() == 's'):
            server_socket.client_socket.send(bytes(self.message, 'utf-8'))
            print("You are a Subscriber")
            Subscriber(server_socket)
        else:
            print("Enter correct role.")
            client()

client()
