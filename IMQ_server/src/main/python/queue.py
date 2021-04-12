class Queue:
    def __init__(self):
        pass

    def create_queue(self):
        self.queue = []

    def push_msg(self, msg):
        self.queue.append(msg)
