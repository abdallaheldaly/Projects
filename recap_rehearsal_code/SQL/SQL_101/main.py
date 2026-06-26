import MySQLdb as db

connection = db.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='password',
            )