from protocol.response_protocol import response_protocol
from datetime import datetime, timedelta
from db.db_con import Db_con
from db.message_db_operation import message_db_operation
import json
from excpetions.connection_exception import *

class Publisher:
    def __init__(self, client_socket, topics):
        try:
            self.response_protocol = response_protocol()
            self.db_con = Db_con.connect_to_db()
            self.topics = topics
            self.client_socket = client_socket
            self.send_topic_to_client()
            self.get_push_request_from_client()
        except Exception as e:
            raise unableToStartServer

    def send_topic_to_client(self):
        self.client_socket.send(bytes(self.response_protocol.json_payload(self.topics), 'utf-8'))

    def get_push_request_from_client(self):
        request = self.client_socket.recv(1024).decode('utf-8')
        json_payload = json.loads(request)
        topic_meta = json_payload["content"].replace(']','').replace('[','').replace("'",'')
        request = topic_meta.split(',')
        expire_time = self.get_expiry_time(int(request[2]))
        message_db_operation.create_message(request, self.db_con, expire_time)

    def get_crrent_timestamp(self):
        ct = datetime.now()
        ts = ct.timestamp()
        return ts

    def get_expiry_time(self, hours):
        return datetime.now() + timedelta(hours=hours)
