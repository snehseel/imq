from db.topic_entity import Topic_entity
from db.db_con import Db_con

class topic_db_operation:
    def create_topic(topic_name, topic_status, my_db):
        try:
            db_cursor = my_db.cursor()
            db_tuple = (topic_name, topic_status)
            db_cursor.execute("INSERT INTO l_c_grad.topic (topic_name, topic_status) VALUES (%s, %s)", (db_tuple))
            my_db.commit()
        except Exception as e:
            raise unableToConnectToDB

    def retrieve_topic(my_db):
        try:
            db_cursor = my_db.cursor()
            db_cursor.execute("SELECT * FROM l_c_grad.topic WHERE topic_status = '1'")
            result = db_cursor.fetchall()
            return result
        except Exception as e:
            raise unableToConnectToDB

    def get_topic_message(my_db, topic_id):
        try:
            db_cursor = my_db.cursor()
            db_cursor.execute("SELECT DISTINCT message_id FROM l_c_grad.msg_topic_mapping WHERE topic_id = %s", (topic_id,))
            result = db_cursor.fetchall()
            return result
        except Exception as e:
            raise unableToConnectToDB

    def remove_topic(my_db, topic_id):
        try:
            db_cursor = my_db.cursor()
            db_cursor.execute("UPDATE l_c_grad.topic SET topic_status = 0 WHERE topic_id = %s", (topic_id,))
            my_db.commit()
        except Exception as e:
            raise unableToConnectToDB

    def purge_topic(my_db, topic_id):
        try:
            db_cursor = my_db.cursor()
            db_cursor.execute("UPDATE l_c_grad.message SET status = 0 WHERE topic_id = %s", (topic_id,))
            my_db.commit()
        except Exception as e:
            raise unableToConnectToDB
