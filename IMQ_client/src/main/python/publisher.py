from protocol.response_protocol import response_protocol
import json
from exceptions.topic_exception import *

class Publisher:
    def __init__(self, server_socket):
        self.server_socket = server_socket
        self.response_protocol = response_protocol()
        self.recieve_topics_from_server()
        self.get_topic_name()

    def recieve_topics_from_server(self):
        try:
            message = self.server_socket.client_socket.recv(1024).decode('utf-8')
            json_payload = json.loads(message)
            topic = json_payload["content"].replace(']','').replace('[','').replace("'",'')
            self.topic = topic.split(',')
            print(self.topic)
        except Exception as e:
            raise unableToFindTopic

    def get_topic_name(self):
        try:
            self.topic_chosen = input("Enter topic Name: ")
            if (self.topic_chosen in self.topic):
                self.push_message()
            else:
                print("Please enter correct topic name: ")
                self.get_topic_name()
        except Exception as e:
            raise unableToFindTopic

    def get_message(self):
        message = input("Enter message to push: ")
        return message

    def get_expiry_time(self):
        expiry_time = input("Enter expiry time of message in hours: ")
        return expiry_time

    def push_message(self):
        try:
            self.message = self.get_message()
            self.expiry_time = self.get_expiry_time()
            self.topic_meta = self.create_list()
            self.server_socket.client_socket.send(bytes(self.response_protocol.json_payload(self.topic_meta), 'utf-8'))
            print("Message pushed to topic sucessfully.")
        except Exception as e:
            raise unableToPushMessage


    def create_list(self):
        return [self.message, self.topic_chosen, self.expiry_time]
