from db.db_con import Db_con
from queue import Queue
from db.topic_db_operation import topic_db_operation
from db.message_db_operation import message_db_operation

class Init_queue:
    def __init__(self):
        pass

    def get_topics(self, db_con):
        self.topics = topic_db_operation.retrieve_topic(db_con)
        return self.topics
