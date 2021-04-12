from db.message_entity import message_entity
from db.db_con import Db_con
from exceptions.db_exceptions import *

class message_db_operation:
    def create_message(message, my_db, expire_time):
        try:
            db_cursor = my_db.cursor()
            db_tuple = (message[0], expire_time)
            db_cursor.execute("INSERT INTO l_c_grad.message (message_content, expire_time) VALUES (%s, %s)", (db_tuple))
            my_db.commit()
        except Exception as e:
            raise unableToConnectToDB

    def create_message_topic_mapping(my_db):
        pass

    def read_message(my_db, topic_name):
        try:
            db_cursor = my_db.cursor()
            db_cursor.execute("SELECT topic_id FROM l_c_grad.topic WHERE topic_name =%s LIMIT 1", (topic_name,))
            result = db_cursor.fetchall()
            db_cursor.execute("SELECT message_content FROM l_c_grad.message LEFT JOIN l_c_grad.msg_topic_mapping ON message.message_id=msg_topic_mapping.message_id WHERE msg_topic_mapping.topic_id = %s", (result[0][0],))
            result = db_cursor.fetchall()
            return result
        except Exception as e:
            raise unableToConnectToDB
