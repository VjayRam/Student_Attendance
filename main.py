import pymysql as sql


def initialize_db():
    conn=sql.connect(host='localhost',user='root',password='root')
    a = conn.cursor()
    db_n = "student_attendance"
    a.execute('create table ' + db_n)
    print('MSG: Database has been initialized successfully!')
    return db_n

def init_table(db_name):
    conn = sql.connect(host='localhost',user='root',password='root',db = db_name)
    a = conn.cursor()
    tab_n = input('Enter Table Name: ')
    q = 'create table '+ tab_n +'(RegNo varchar(5) PRIMARY KEY, name varchar(25), sec varchar(2), gender varchar(2), dob date, );'
    a.execute()
    return
