from db.client_entity import client_entity
from db.db_con import Db_con
from exceptions.db_exceptions import *

class client_db_operation:
    def create_client(client_addr, role, my_db):
        try:
            db_cursor = my_db.cursor()
            db_tuple = (client_addr[0], client_addr[1], role)
            db_cursor.execute("INSERT INTO l_c_grad.client (address, port, role) VALUES (%s, %s, %s)", (db_tuple))
            my_db.commit()
        except Exception as e:
            raise unableToConnectToDB

    def retrieve_client(my_db, client_type):
        try:
            db_cursor = my_db.cursor()
            db_cursor.execute("SELECT * FROM l_c_grad.client WHERE role = %s", (client_type,))
            result = db_cursor.fetchall()
            return result
        except Exception as e:
            raise unableToConnectToDB
            
