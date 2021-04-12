class unableToPushToQueue(Exception):
    def __init__(self):
        self.msg = "Unable to push message to queue"
        super().__init__(self.msg)

class queueNotFound(Exception):
    def __init__(self):
        self.msg = "Queue not found"
        super().__init__(self.msg)