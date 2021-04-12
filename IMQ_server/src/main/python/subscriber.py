from protocol.response_protocol import response_protocol
from datetime import datetime, timedelta
from db.db_con import Db_con
from db.message_db_operation import message_db_operation
import json
from exceptions.connection_exception import *

class Subscriber:
    def __init__(self, client_socket, topics):
        try:
            self.response_protocol = response_protocol()
            self.db_con = Db_con.connect_to_db()
            self.topics = topics
            self.client_socket = client_socket
            self.send_topic_to_client()
            self.get_pull_request_from_client()
            self.send_msg_to_client()
        except Exception as e:
            raise unableToStartServer


    def send_topic_to_client(self):
        self.client_socket.send(bytes(self.response_protocol.json_payload(self.topics), 'utf-8'))

    def get_pull_request_from_client(self):
        request = self.client_socket.recv(1024).decode('utf-8')
        json_payload = json.loads(request)
        self.result = message_db_operation.read_message(self.db_con, str(json_payload['content']))

    def send_msg_to_client(self):
        self.client_socket.send(bytes(self.response_protocol.json_payload(self.result), 'utf-8'))
