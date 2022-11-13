import streamlit as st
import mysql.connector 
from database import create_table

def main():
    st.title("Student Attendance System")
    menu = ["Take Attendance", "Update Attendance List", "View Attendance List", "Remove List"]
    choice = st.sidebar.selectbox("Menu",menu)
    create_table()
    if choice == "Take Attendance":
        return
    elif choice == "Update Attendance List":
        return
    elif choice == "View Attendance List":
        return
    else:
        return

if __name__ == "__main__":
    main()