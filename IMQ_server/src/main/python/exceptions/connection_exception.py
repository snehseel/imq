class unableToStartServer(Exception):
    def __init__(self):
        self.msg = "Unable to start the server"
        super().__init__(self.msg)