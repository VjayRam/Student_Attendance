import streamlit as st
import mysql.connector
from database import about
from database import create_table, edit_details

def main():
    st.title("Student Attendance System")
    menu = ["Attendance", "Add Details", "View Details", "Update Details", "Remove Details","Credits"]
    ch = st.sidebar.selectbox("Menu",menu)
    create_table()
    if ch == "Attendance":
        about()
    elif ch == "Add Details":
        about()
    elif ch == "View Details":
        about()
    elif ch == "Update Details":
        about()
    elif ch == "Remove Details":
        about()
    else:
        about()

if __name__ == "__main__":
    main()