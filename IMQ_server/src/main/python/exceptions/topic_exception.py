class unableToCreateTopic(Exception):
    def __init__(self):
        self.msg = "Unable to create topic"
        super().__init__(self.msg)