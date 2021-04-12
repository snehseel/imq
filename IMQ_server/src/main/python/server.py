import socket
from functools import partial
from db.db_con import Db_con
from server_socket import new_socket
from _thread import start_new_thread
from publisher import Publisher
from subscriber import Subscriber
from initialize_queue_from_db import Init_queue
from db.client_db_operation import client_db_operation
from exceptions.connection_exception import *

class Server:

    def __init__(self):
        server_socket = new_socket()
        server_socket.new_socket.listen(10)
        self.db_con = Db_con.connect_to_db()
        print("Fetching data from DB")
        self.queue = Init_queue()
        topic = self.queue.get_topics(self.db_con)
        print("Following Topics are ready.")
        self.topics = []
        for row in topic:
            print(row[0])
            self.topics.append(row[0])
        while True:
            self.client_socket, self.client_address = server_socket.new_socket.accept()
            print(self.client_address)
            try:
                start_new_thread(self.recieve_role, (self.client_socket, self.client_address))
            except Exception as e:
                raise unableToStartServer

    def recieve_role(self, client_socket, client_address):
        message = self.client_socket.recv(1024).decode('utf-8')
        print("connection with ", self.client_address)
        client_db_operation.create_client(self.client_address, message.lower(), self.db_con)
        if message.lower() == 'p':
            print("client is a: PUBLISHER")
            self.role = 'p'
            Publisher(self.client_socket, self.topics)
        elif message.lower() == 's':
            print("client is a: SUBSCRIBER")
            self.role = 's'
            Subscriber(self.client_socket, self.topics)

Server()
