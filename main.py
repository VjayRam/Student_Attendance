import pymysql as sql


def initialize_db():
    conn=sql.connect(host='localhost',user='root',password='root')
    a = conn.cursor()
    db_n = "student_attendance"
    a.execute('create table ' + db_n)
    print('MSG: Database has been initialized successfully!')
    return db_n

def init_class_table(db_name):
    conn = sql.connect(host='localhost',user='root',password='root',db = db_name)
    a = conn.cursor()
    cl_n = int(input('Enter Class (1-12): '))
    if (cl_n >= 1 and cl_n <= 12):
        q = 'create table class'+ str(cl_n) +'(sections varchar(5) PRIMARY KEY, t_count int, b_count int, g_count int, incharge varchar(25));'
        a.execute(q)
    else:
        print('ERROR: Enter only numbers between 1 to 12 as input')
    return

def init_sec_table(db_name):
    conn = sql.connect(host='localhost',user='root',password='root',db = db_name)
    a = conn.cursor()
    sec_n = input('Enter Section: ')


