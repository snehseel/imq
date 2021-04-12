class unableToConnect(Exception):
    def __init__(self):
        self.msg = "Unable to connect to server"
        super().__init__(self.msg)

class portBlocked(Exception):
    def __init__(self):
        self.msg = "Port is blocked"
        super().__init__(self.msg)

class unableToRetrieveMessage(Exception):
    def __init__(self):
        self.msg = "Unable to retrieve message from the topic"
        super().__init__(self.msg)