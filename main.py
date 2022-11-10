import mysql.connector as sql


def initialize_db():
    conn=sql.connect(host='localhost',user='root',password='root')
    a = conn.cursor()
    db_n = "student_attendance"
    a.execute('create database ' + db_n)
    print('MSG: Database has been initialized successfully!')
    return db_n

def init_tables(db_name):
    conn = sql.connect(host='localhost',user='root',password='root',db = db_name)
    a = conn.cursor()

def init_sec_table(db_name):
    conn = sql.connect(host='localhost',user='root',password='root',db = db_name)
    a = conn.cursor()
    sec_n = input('Enter Section: ')


