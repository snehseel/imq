from db.db_con import Db_con
from db.topic_db_operation import topic_db_operation
from db.message_db_operation import message_db_operation
from db.client_db_operation import client_db_operation
from admin_helper_func import Admin_helper_function
from exceptions.db_exceptions import *

class Admin_operations:

    def create_topic(self, db_con):
        try:
            topic_name = Admin_helper_function.get_topic_name(self)
            topic_db_operation.create_topic(topic_name, 1, db_con)
            print("Topic Created")
        except:
            raise unableToConnectToDB

    def remove_topic(self, db_con):
        try:
            Admin_helper_function.show_topic_list(self, db_con)
            topic_id = Admin_helper_function.get_topic_name(self)
            topic_db_operation.remove_topic(db_con, topic_id)
            print("Topic Removed")
        except:
            raise unableToConnectToDB

    def restrict_topic(self, db_con):
        try:
            Admin_helper_function.show_topic_list(self, db_con)
            topic_id = Admin_helper_function.get_topic_name(self)
            topic_db_operation.remove_topic(db_con, topic_id)
            print("Topic Removed")
        except:
            raise unableToConnectToDB

    def purge_topic(self, db_con):
        try:
            Admin_helper_function.show_topic_list(self, db_con)
            topic_id = Admin_helper_function.get_topic_name(self)
            topic_db_operation.remove_topic(db_con, topic_id)
            topic_db_operation.purge_topic(db_con, topic_id)
            print("Topic Purged")
        except:
            raise unableToConnectToDB

    def show_subscribers(self, db_con):
        try:
            subscribers = client_db_operation.retrieve_client(db_con, 's')
            for row in subscribers:
                print(row)
        except:
            raise unableToConnectToDB

    def show_publishers(self, db_con):
        try:
            publishers = client_db_operation.retrieve_client(db_con, 'p')
            for row in publishers:
                print(row)
        except:
            raise unableToConnectToDB
