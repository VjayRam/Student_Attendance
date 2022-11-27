import mysql.connector
import streamlit as st
from datetime import date
import pandas as pd

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="attendance_se")
c = mydb.cursor()

def about():
    st.header("About the Project")
    st.text('This is a project done by 5th Semester students of CSE Department, PES University \nfor Software Engineering Course (UE20CS303).')
    st.subheader('Features:')
    st.text('The project has been designed for Schools and Colleges to maintain and update the \nattendance records of students.')
    st.subheader('Credits:')
    st.markdown('- ***Mentor*** : Venkatesh Prasad ***(Professor)***')
    st.markdown('- ***Student 1*** : Rachana R ***(PES1UG20CS677)***')
    st.markdown('- ***Student 2*** : Vijay Ram E ***(PES1UG20CS700)***')
    st.markdown('- ***Student 3*** : Sai Deepika P ***(PES1UG20CS718)***')
    st.markdown('- ***Student 4*** : Sneha Saravanan ***(PES1UG20CS721)***')
            
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Student ( Student_ID varchar(10) unique, Fname varchar(20), Lname varchar(20), Age int NOT NULL, DOB date, Pincode int, Class int, Section varchar(5), Parent_ph bigint, primary key(Student_ID));")
    c.execute("CREATE TABLE IF NOT EXISTS Teacher ( Teacher_ID varchar(10) unique, Fname varchar(20), Lname varchar(20), Age int NOT NULL, Class int, Ph_no varchar(10), Email varchar(30), primary key(Teacher_ID));")
    c.execute("CREATE TABLE IF NOT EXISTS Attendance (Student_ID varchar(10), Class int, Section varchar(5), Teacher_ID varchar(10), Att_date datetime, Attendance char default 'N', foreign key(Teacher_ID) references Teacher(Teacher_ID), foreign key(Student_ID) references Student(Student_ID));")

def add_details():
    opt = ["Add Student", "Add Teacher"]
    x = st.selectbox("Add:",opt)
    if x == "Add Student":
        st.subheader("Enter Student Details:")
        
        col1, col2 = st.columns(2)
        with col1:
            sid = st.text_input("Enter Student ID: ")
            fname = st.text_input("Enter First Name: ")
            lname = st.text_input("Enter Last Name: ")
            cl = st.radio("Choose Class: ",["1","2","3","4","5","6","7","8","9","10","11","12"])
        with col2:
            dob = st.date_input("Enter DOB: ")
            pin = st.text_input("Enter Pincode: ")
            ph = st.number_input("Enter Parent Phone Number: ")
            sec = st.radio("Choose Section: ",["A","B","C","D","E","F","G","H","I","K","L"]) 
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)) 
        
        if st.button("Add Student"):
            c.execute("insert into student( Student_ID ,Fname,Lname ,Age ,DOB ,Pincode ,Class ,Section ,Parent_ph) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);", (sid, fname, lname, age, dob, pin, cl, sec, ph))
            st.success("Successfully added student: {}".format(sid))

    elif x == "Add Teacher":
        st.subheader("Enter Teacher Details:")
        col1, col2 = st.columns(2)
        with col1:
            tid = st.text_input("Enter Teacher ID: ")
            fname = st.text_input("Enter First Name: ")
            lname = st.text_input("Enter Last Name: ")
            age = st.number_input("Enter Age: ")
            email = st.text_input("Enter Email: ")
        with col2:
            cl = st.radio("Choose Class: ",["1","2","3","4","5","6","7","8","9","10","11","12"])
            ph = st.number_input("Enter Phone Number: ")
        if st.button("Add Teacher"):
            c.execute("insert into Teacher(Teacher_ID ,Fname,Lname ,Age ,Class ,Phone ,Email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);", (tid, fname, lname, age, cl, ph, email))
            st.success("Successfully added teacher: {}".format(tid))
    else:
        about()

def view_details():
    opt = ["View Student", "View Teacher"]
    x = st.selectbox("View:",opt)
    if x == "View Student":
        st.subheader("View Student Details:")
        sid = st.text_input("Enter Student ID: ")
        c.execute("select * from Student where Student_ID = '"+sid+"';")
        data = c.fetchall()
        st.dataframe(data)     
    elif x == "View Teacher":
        st.subheader("View Teacher Details:")
        tid = st.text_input("Enter Teacher ID: ")
        c.execute("select * from Teacher where Teacher_ID = '"+tid+"';")
        data = c.fetchall()
        st.dataframe(data)
    else:
        about()

def edit_details():
    opt = ["Edit Student", "Edit Teacher"]
    x = st.selectbox("Edit:",opt)
    if x == "Edit Student":
        st.subheader("Edit Student Details:")
        sid = st.text_input("Enter Student ID: ")
        c.execute("select * from Student where Student_ID = '"+sid+"';")
        data = c.fetchall()
        df = pd.DataFrame(data, columns=['Student_ID' ,'Fname','Lname' ,'Age' ,'DOB' ,'Pincode' ,'Class' ,'Section' ,'Parent_Phone'])
        st.subheader("Current Student Details:")
        st.dataframe(df)
        st.subheader("Enter New Student Details:")
        col1, col2 = st.columns(2)
        with col1:
            pin = st.text_input("Enter New Pincode: ")
            cl = st.radio("Choose New Class: ",["1","2","3","4","5","6","7","8","9","10","11","12"])
        with col2:
            ph = st.number_input("Enter New Parent Phone Number: ")
            sec = st.radio("Choose New Section: ",["A","B","C","D","E","F","G","H","I","K","L"])
    
        if st.button("Update Details"):    
            c.execute("UPDATE Student SET Pincode=%s, Class=%s, Section=%s, Parent_ph=%s WHERE "
              "Student_ID=%s", (pin, cl, sec, ph, sid))
            mydb.commit()
            st.success("Successfully Updated Student: {}".format(sid))
        #about()
    elif x == "Edit Teacher":
        st.subheader("Edit Teacher Details:")
        tid = st.text_input("Enter Teacher ID: ")
        c.execute("select * from Teacher where Teacher_ID = '"+tid+"';")
        data = c.fetchall()
        df = pd.DataFrame(data, columns=['Teacher_ID' ,'Fname','Lname' ,'Ph_no' ,'Email' ,'Class'])
        st.subheader("Current Teacher Details:")
        st.dataframe(df)
        st.subheader("Enter New Teacher Details:")
        col1, col2 = st.columns(2)
        with col1:
            email = st.text_input("Enter New Email: ")
            ph = st.number_input("Enter New Phone Number: ")
        with col2:
            cl = st.radio("Choose New Class: ",["1","2","3","4","5","6","7","8","9","10","11","12"])
        
        if st.button("Update Details"): 
            c.execute("UPDATE Teacher SET Ph_no=%s, Email=%s, Class=%s WHERE Teacher_ID=%s", (ph, email, cl, tid))
            mydb.commit()
            st.success("Successfully Updated Teacher: {}".format(tid))
        #about()
    else:
        about()

def del_details():
    opt = ["Remove Student", "Remove Teacher"]
    x = st.selectbox("Remove:",opt)

    if x == "Remove Student":
        st.subheader("Edit Student Details:")
        sid = st.text_input("Enter Student ID: ")
        st.warning("Do you want to delete ::{}".format(sid))
        if st.button("Remove Student"):
            c.execute('DELETE FROM Student WHERE Student_ID="{}"'.format(sid))
            mydb.commit()
            st.success("Student {} deleted".format(sid))
    elif x == "Remove Teacher":
        st.subheader("Edit Teacher Details:")
        tid = st.text_input("Enter Teacher ID: ")
        st.warning("Do you want to delete ::{}".format(tid))
        if st.button("Remove Teacher"):
            c.execute('DELETE FROM Teacher WHERE Teacher_ID="{}"'.format(tid))
            mydb.commit()
            st.success("Teacher {} deleted".format(tid))
    else:
        about()

def attendance():
    menu = ["Take Attendance", "View Attendance", "Update Attendance"]
    a = st.sidebar.selectbox("Attendance:", menu)
    
    return
