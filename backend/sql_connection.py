import mysql.connector

__cnx = None


def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='S4xt0n18',
                                        host='127.0.0.1',
                                        database='Shopping_Cart')
    return __cnx
