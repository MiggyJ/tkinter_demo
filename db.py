import mysql.connector as conn

class Database:
    def __init__(self):
        try:
            self.conn = conn.connect(
                host='localhost',
                database='tkinter_demo',
                user='root',
                password=''
            )
            self.cursor = self.conn.cursor(dictionary=True)
        except Exception as e:
            print(e)

    def getAllTasks(self):
        try:
            self.cursor.execute('SELECT * FROM TASKS')
            res = self.cursor.fetchall()
            return res
        except Exception as e:
            print(e)

db = Database()
tasks = db.getAllTasks()
print(tasks)