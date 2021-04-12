class unableToConnectToDB(Exception):
    def __init__(self):
        self.msg = "Unable to connect to DB"
        super().__init__(self.msg)
