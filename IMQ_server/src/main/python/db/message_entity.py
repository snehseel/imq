class message_entity:
    def message_content(self, value):
        self.message_content = value

    def message_publisher(self, value):
        self.message_publisher = value

    def message_create_time(self, value):
        self.message_create_time = value

    def message_expiry_time(self, value):
        self.message_expiry_time = value

    def message_status_setter(self, value):
        self.message_status = value

    def message_dictionary(self):
        self.message = {
            "content": self.message_content,
            "publisher": self.message_publisher,
            "create": self.message_create_time,
            "expiry": self.message_expiry_time,
            "status": self.message_status
        }
