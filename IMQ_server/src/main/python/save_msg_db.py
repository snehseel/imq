from excpetions.connection_exception import *

class db_operations:
    def save_user(client_addr, my_db):
        try:
            db_cursor = my_db.cursor()
            db_tuple = (str(client_addr[0]), str(client_addr[1]))
            db_cursor.execute("INSERT INTO l_c_grad.client (address, port) VALUES (%s, %s)", (db_tuple))
            my_db.commit()
        except Exception as e:
            raise unableToConnectToDB


    def save_message(client_addr, arr[]):
        try:
            db_cursor = arr[0].cursor()
            db_tuple = (str(client_addr[0]) + '_' + str(client_addr[1]), arr[1])
            db_cursor.execute("INSERT INTO l_c_grad.message values (%s, %s)", (db_tuple))
            arr[0].commit()
        except Exception as e:
            raise unableToConnectToDB


    def save_topic(client_addr, arr[]):
        try:
            db_cursor = arr[0].cursor()
            db_tuple = (str(client_addr[0]) + '_' + str(client_addr[1]), arr[1])
            db_cursor.execute("INSERT INTO l_c_grad.message values (%s, %s)", (db_tuple))
            arr[0].commit()
        except Exception as e:
            raise unableToConnectToDB


    def delete_topic(arr[]):
        try:
            db_cursor = arr[0].cursor()
            db_tuple = ()
            db_cursor.execute()
            aarr[0].commit()
        except Exception as e:
            raise unableToConnectToDB


    def purge_topic(client_addr, arr[]):
        try:
            db_cursor = arr[0].cursor()
            db_tuple = (str(client_addr[0]) + '_' + str(client_addr[1]), arr[1])
            db_cursor.execute("INSERT INTO l_c_grad.message values (%s, %s)", (db_tuple))
            arr[0].commit()
        except Exception as e:
            raise unableToConnectToDB
