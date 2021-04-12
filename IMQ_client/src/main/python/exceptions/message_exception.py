class messageFormatException(Exception):
    def __init__(self):
        self.msg = "Message format is not correct. Expected format is either JSON or XML"
        super().__init__(self.msg)