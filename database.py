import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="attendance_se"
)
c = mydb.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Student ( Student_ID varchar(10) unique, Fname varchar(20), Lname varchar(20), Age int NOT NULL, DOB date, Pincode int, Class int, Section varchar(5), Parent_ph bigint, primary key(Student_ID));")
    c.execute("CREATE TABLE IF NOT EXISTS Teacher ( Teacher_ID varchar(10) unique, Fname varchar(20), Lname varchar(20), Ph_no varchar(10), Email varchar(30), primary key(Teacher_ID));")
    c.execute("CREATE TABLE IF NOT EXISTS Subjects ( Sub_ID varchar(10) unique, Sub_name varchar(25), Class int, primary key(Sub_ID));")
    c.execute("CREATE TABLE IF NOT EXISTS Student_Subject ( Student_ID varchar(10), Student_name varchar(20), Sub_ID varchar(10), Class int, foreign key(Student_ID) references Student(Student_ID), foreign key(Sub_ID) references Subjects(Sub_ID));")
    c.execute("CREATE TABLE IF NOT EXISTS Subject_Teacher (Sub_ID varchar(10), Teacher_ID varchar(10), Class int, foreign key(Sub_ID) references Subjects(Sub_ID), foreign key(Teacher_ID) references Teacher(Teacher_ID));")
    c.execute("CREATE TABLE IF NOT EXISTS Attendance (Student_ID varchar(10), Class int, Section varchar(5), Sub_ID varchar(10), Teacher_ID varchar(10), Class_DateTime datetime, Attendance char default 'N', foreign key(Teacher_ID) references Teacher(Teacher_ID), foreign key(Sub_ID) references Subjects(Sub_ID), foreign key(Student_ID) references Student(Student_ID));")
  

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