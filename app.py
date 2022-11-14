import streamlit as st
import mysql.connector
from database import about
from database import create_table

def main():
    st.title("Student Attendance System")
    menu = ["Take Attendance", "Update Attendance List", "View Attendance List", "Remove List","Credits"]
    ch = st.sidebar.selectbox("Menu",menu)
    create_table()
    if ch == "Take Attendance":
        about()
    elif ch == "Update Attendance List":
        about()
    elif ch == "View Attendance List":
        about()
    elif ch == "Remove List":
        about()
    else:
        about()

if __name__ == "__main__":
    main()