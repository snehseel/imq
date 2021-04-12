class unableToFindTopic(Exception):
    def __init__(self):
        self.msg = "Topic does not exist"
        super().__init__(self.msg)

class unableToPushMessage(Exception):
    def __init__(self):
        self.msg = "Unable to pull message from topic"
        super().__init__(self.msg)
    
class unableToPullMessage(Exception):
    def __init__(self):
        self.msg = "Unable to push message to topic"
        super().__init__(self.msg)

class unableToSubscribeTopic(Exception):
    def __init__(slef):
        self.msg = "Unable to subscribe to the topic"
        super().__init__(self.msg)