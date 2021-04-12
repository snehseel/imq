from protocol.response_protocol import response_protocol
import json

class Subscriber:
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
            raise unableToSubscribeTopic


    def get_topic_name(self):
        try:
            self.topic_chosen = input("Enter topic Name: ")
            if (self.topic_chosen in self.topic):
                self.get_messages()
            else:
                print("Please enter correct topic name: ")
                self.get_topic_name()
        except Exception as e:
            raise unableToSubscribeTopic

    def get_messages(self):
        try:
            self.server_socket.client_socket.send(bytes(self.response_protocol.json_payload(self.topic_chosen), 'utf-8'))
            message = self.server_socket.client_socket.recv(1024).decode('utf-8')
            json_payload = json.loads(message)
            messages = self.sanitize_msg(json_payload)
            print("Messages are: ",messages)
        except Exception as e:
            raise unableToPullMessage


    def sanitize_msg(self, json_payload):
        messages = json_payload["content"].replace(')]','').replace('[(','').replace("'",'').replace('(','').replace(",)",'')
        messages = messages.split(',')
        return messages
