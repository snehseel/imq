from db.topic_db_operation import topic_db_operation

class Admin_helper_function:
    def __init__(self):
        pass

    def get_topic_name(self):
        topic_name = input("Enter topic Name: ")
        return topic_name

    def get_topic_id(self):
        topic_id = input("Enter Topic ID: ")
        return topic_id

    def show_topic_list(self, db_con):
        topics = topic_db_operation.retrieve_topic(db_con)
        print("Topic Name \t Topic ID \t Topic Status")
        for row in topics:
            print(str(row[0]) + "\t \t \t" + str(row[1]) + "\t \t" + str(row[2]))
