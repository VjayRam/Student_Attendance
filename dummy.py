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

def search():
    conn=sql.connect(host='localhost',user='root',password='manager',db='Emp')
    a=conn.cursor()
    r=int(input('Enter Employee ID:'))
    print('1 . Name')
    print('2 . Company')
    print('3 . Designation')
    print('4 . All Details')
    q=int(input(':::What Would you like to search?:::'))
    if q==1:
         a.execute('select Name from emp where ID="'+ str(r)+'"');
         data=a.fetchall()
         x=data[0]
         print('Name of the employee is: ', x)
         conn.commit()
         #Searching only Names of Employees..
    elif q==2:
         a.execute('select Company from emp where ID="'+ str(r)+'"');
         data=a.fetchall()
         x=data[0]
         print('Company of the Employee: ', x)
         conn.commit()
         #Searching only Company of Employees..
    elif q==3:
         a.execute('select Designation from emp where ID="'+ str(r)+'"');
         data=a.fetchall()
         x=data[0]
         print('Designation of the employee: ', x)
         conn.close()
         #Searching only Designation of Employees..
    elif q==4:
        query='select * from emp where id='+str(r);
        a.execute(query)
        data=a.fetchall()
        
        if(data):
            print('Existing details are::')
            L=[]
            for i in data:
                for j in i:
                    L.append(j)
            print('ID= ',L[0])
            print('Name= ',L[1])
            print('Company= ',L[2])
            print('Date of birth= ',L[3])
            print('Salary= ',L[4])
            print('Contact= ',L[5])
            print('Designation= ',L[6])
        conn.commit()
    #Searching all Details of an Employee..
    else:
        print('::::Details not found!!::::')
        conn.commit()

def insert():
    conn=sql.connect(host='localhost',user='root',password='manager',db='Emp')
    a=conn.cursor()
    r=int(input('Enter ID: '))
    n=input('Enter Name: ')
    m=input('Enter Company: ')
    d=input('Enter DOB: ')
    p=int(input('Enter Salary: '))
    sa=int(p/30)
    q=int(input('Enter Contact: '))
    s=input('Enter Designation: ')
    query='insert into emp(ID,Name,Company,DOB,Monthly_salary,salary_per_day,Contact_no,Designation) values ('+str(r)+',"'+n+'","'+m+'","'+d+'",'+str(p)+','+str(sa)+','+str(q)+',"'+s+'");'
    a.execute(query)
    #Inserts only values in selected columns..
    print('Succesfully Inserted Employee Details')
    conn.commit()


def disp():
    conn=sql.connect(host='localhost',user='root',password='manager',db='Emp')
    a=conn.cursor()
    print('1 . Infosys')
    print('2 . Google')
    print('3 . HP')
    b=int(input('Enter Employee company: '))
    if b==1:
        a.execute("select * from emp where company='Infosys'")
    #Displaying only Infosys Employees..
    if b==2:
        a.execute("select * from emp where company='Google'")
    #Displaying only Google Employees..
    if b==3:
         a.execute("select * from emp where company='HP'")
    #Displaaying only HP Employees..
    else:
         print("::::Choose The right option::::")
    data=a.fetchall()
    for i in data:
        for j in i:
            print(j,end='\t')
        print()
    conn.commit()

def leaves():
    conn=sql.connect(host='localhost',user='root',password='manager',db='Emp')
    a=conn.cursor()
    b=input('Enter your employee ID number')
    q=int(input('Applying leave for how many days?'))
    query1='update emp set leaves="'+str(q)+'" where ID='+str(b);
    query2='update emp set lop=leaves*salary_per_day;'
    a.execute(query1)
    a.execute(query2)
    conn.commit()
    conn=sql.connect(host='localhost',user='root',password='manager',db='Emp')
    a=conn.cursor()
    query3='select lop from emp where id="'+str(b)+'"'
    a.execute(query3)
    c=a.fetchall()
    lop=c[0][0]
    print('Pay Deducted by: ',lop)
    #Loss of pay = no of days of leave * salary per day
    conn.commit()
   


def update():
    conn=sql.connect(host='localhost',user='root',password='manager',db='Emp')
    a=conn.cursor()
    r=int(input('Enter ID of employee to be updated: '))
    print('1. Company name')
    print('2. Salary')
    print('3. Contact number')
    print('4. Designation')
    print('5. Update all')
    k=int(input('Select what to update: '))
    if k==1:
        co=input('Enter New Company Name: ')
        query1='update emp set Company="'+co+'" where ID='+str(r);
        a.execute(query1)
        print('Company Name updated Sucessfully')
        conn.commit()
        #Updates only Company name..
    elif k==2:
        sa=input('Enter Updated Salary: ')
        query2='update emp set monthly_salary="'+sa+'"where ID='+str(r);
        queryk='update emp set salary_per_day=monthly_salary/30';
        a.execute(query2)
        a.execute(queryk)
        print('Salary Updated Successfully')
        #Updates only Salary..
        conn.commit()
    elif k==3:
        con=int(input('Enter new Contact Number: '))
        query3='update emp set Contact_No='+str(con)+' where ID='+str(r);
        a.execute(query3)
        print('Contact updated successfully')
        conn.commit()
        #Updates only Contact number..
    elif k==4:
        des=input('Enter new Designation: ')
        query4='update emp set Designation="'+des+'" where ID='+str(r);
        a.execute(query4)
        print('Designation updated successfully')
        conn.commit()
        #Updates only Designation..
    elif k==5:
        query5='Select ID,Name,Company,DOB,Monthly_salary,Contact_no,Designation from emp where ID= '+str(r);
        a.execute(query5)
        data=a.fetchall()
        if(data):                
            print('Existing details are::')
            L=[]
            for i in data:
                for j in i:
                    L.append(j)
            print('ID= ',L[0])
            print('Name= ',L[1])
            print('Company= ',L[2])
            print('Date of birth= ',L[3])
            print('Salary= ',L[4])
            print('Contact= ',L[5])
            print('Designation= ',L[6])
            print('\n:::Enter the new details:::')
            n=input('Enter new Name: ')
            m=input('Enter new Company: ')
            d=input('Enter new Date of birth: ')
            p=int(input('Enter new Salary: '))
            q=int(input('Enter new Contact: '))
            t=input('Enter new Designation: ')
        #Prints all the Existing details first..
        query1="update emp set name='"+n+"',company='"+m+"',dob='"+d+"',Monthly_salary="+str(p)+",contact_no="+str(q)+",designation='"+t+"' where id="+str(r)
        #To update name,company,dob,salary,contact_no,designation when an ID is given..
        query2='update emp set salary_per_day=Monthly_salary/30';
        #This updates the salary per day according to the changes made in the monthly salary..
        a.execute(query1)
        print('::::Employee Details Updated successfully::::!!')
        conn.commit()
    else:
        print('ID' ,r,'doesnt exists')
        conn.commit()

def delete():
    conn=sql.connect(host='localhost',user='root',password='manager',db='Emp')
    a=conn.cursor()
    r=input('Enter ID of Employee to Delete details: ')
    a.execute('select * from emp where ID='+r)
    data=a.fetchall()
    if(data):
        ch=int(input("Are you sure to delete entire row's content? \nPress 1 if yes\nPress any other number if no !"))
    #Clicking on 1 clears the entire row's contents..Clicking on any other number keeps the row as it is..
        if(ch==1):
            query='delete from emp where ID= '+r
            a.execute(query)
            print('ID ',r,' Details have been deleted successfully.')
            conn.commit()
        else:
            print('ID',r,'Details left untouched as per Received Instruction')
    else:
            print('ID ',r,' Does not exist::')
print("\n"*19)
print("\t\t\t\t      :::::: WELCOME TO IT TECHPARK, BANGALORE :::::\t\t\t\t\t\t")
print("\t\t\t\t\t:::EMPLOYEE MANAGEMENT SYSTEM:::\t\t\t\t\t\t")
while(1):
    print("\t\t\t1. Create Db or Table")
    print("\t\t\t2. Insert Details")
    print("\t\t\t3. Apply For Leaves")
    print("\t\t\t4. Update Details")
    print("\t\t\t5. Display Details")
    print("\t\t\t6. Search Details")
    print("\t\t\t7. Delete Details")
    print("\t\t\t8. Exit screen")
    #print("\n"*3)
    ch=int(input('Enter choice: '))
    if(ch==1):
        create()
    elif(ch==2):
        insert()
    elif(ch==3):
        leaves()
    elif(ch==4):
        update()
    elif(ch==5):
        disp()
    elif(ch==6):
        search()
    elif(ch==7):
        delete()
    else:
        print('\n'*20)
        print('\t\t\tThanks For using Employee Payroll Database Management Software')
        print('\t\t\t\t\t©Sri Chaitanya 2020')
        print('\n'*10)
        break  
