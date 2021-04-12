import json

class response_protocol:

    def __init__(self):
        self.get_message_content = None
        self.version = None
        self.source_address = None
        self.destination_address = None
        self.error_code = None
        self.status = None

    def get_message_content(self):
        return self.message_content

    def set_message_content(value):
        self.message_content = value

    def get_version(self):
        return self.version

    def set_version(self, value):
        self.version = value

    def get_source_address(self):
        return self.source_address

    def set_source_address(value):
        self.source_address = value

    def get_destination_address(self):
        return self.destination_address

    def set_destination_address(value):
        self.destination_address = value

    def get_error_code(self):
        self.error_code = value

    def set_error_code(value):
        return self.error_code

    def json_payload(self, content):
        self.set_version("1.0")
        json_payload = {"version":self.get_version(),"content":str(content),"src_addr":"test","dest_addr":"test","error_code":"none"}
        return json.dumps(json_payload)
