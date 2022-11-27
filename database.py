import mysql.connector
import streamlit as st
from datetime import date

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="attendance_se")
c = mydb.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Student ( Student_ID varchar(10) unique, Fname varchar(20), Lname varchar(20), Age int NOT NULL, DOB date, Pincode int, Class int, Section varchar(5), Parent_ph bigint, primary key(Student_ID));")
    c.execute("CREATE TABLE IF NOT EXISTS Teacher ( Teacher_ID varchar(10) unique, Fname varchar(20), Lname varchar(20), Ph_no varchar(10), Email varchar(30), primary key(Teacher_ID));")
    c.execute("CREATE TABLE IF NOT EXISTS Subjects ( Sub_ID varchar(10) unique, Sub_name varchar(25), Class int, primary key(Sub_ID));")
    c.execute("CREATE TABLE IF NOT EXISTS Student_Subject ( Student_ID varchar(10), Student_name varchar(20), Sub_ID varchar(10), Class int, foreign key(Student_ID) references Student(Student_ID), foreign key(Sub_ID) references Subjects(Sub_ID));")
    c.execute("CREATE TABLE IF NOT EXISTS Subject_Teacher (Sub_ID varchar(10), Teacher_ID varchar(10), Class int, foreign key(Sub_ID) references Subjects(Sub_ID), foreign key(Teacher_ID) references Teacher(Teacher_ID));")
    c.execute("CREATE TABLE IF NOT EXISTS Attendance (Student_ID varchar(10), Class int, Section varchar(5), Sub_ID varchar(10), Teacher_ID varchar(10), Class_DateTime datetime, Attendance char default 'N', foreign key(Teacher_ID) references Teacher(Teacher_ID), foreign key(Sub_ID) references Subjects(Sub_ID), foreign key(Student_ID) references Student(Student_ID));")

def add_details():
    opt = ["Add Student", "Add Teacher", "Add Subject"]
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
            ph = st.number_input("Enter Phone Number: ")
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
            c.execute("insert into Teacher( Teacher_ID ,Fname,Lname ,Age ,Class ,Phone ,Email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);", (tid, fname, lname, age, cl, ph, email))
            st.success("Successfully added teacher: {}".format(tid))
    else:
        pass




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