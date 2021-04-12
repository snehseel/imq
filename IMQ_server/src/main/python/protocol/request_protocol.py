class request_protocol:

    def __init__(self):
        self.request_type = None
        self.message_content = None
        self.version = None
        self.source_address = None
        self.destination_address = None

    def set_request_type(value):
        self.request_type = value

    def get_request_type(self):
        return self.request_type

    def get_message_content(self):
        return self.message_content

    def set_message_content(value):
        self.message_content = value

    def get_version(self):
        return self.version

    def set_version(value):
        self.version = value

    def get_source_address(self):
        return self.source_address

    def set_source_address(value):
        self.source_address = value

    def get_destination_address(self):
        return self.destination_address

    def set_destination_address(value):
        self.destination_address = value
