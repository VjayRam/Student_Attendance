import pymysql as sql


def create():
    print("a.Create new database")
    print("b.Create new table")
    ch1=input('Enter your choice')
    if(ch1=='a'):
        db_create()
    elif(ch1=='b'):
        tab_create()
    else:
        print("Invalid choice::")

def db_create():
    conn=sql.connect(host='localhost',user='root',password='manager')
    a=conn.cursor()
    db_name=input('Enter db name:')
    a.execute('create database '+db_name)
    print('Database has been created successfully')
    return db_name
    conn.commit()

def tab_create():
    conn=sql.connect(host='localhost',user='root',password='manager',db='Emp')
    a=conn.cursor()
    tab_name=input('Enter table name:')
    a.execute('create table '+tab_name+'( ID int primary key,Name varchar(20),Company varchar(25),DOB date,Salary int,Contact int(15),Designation varchar(25));')
    print('Table has been created successfully')
    conn.commit()

