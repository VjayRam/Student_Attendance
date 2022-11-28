import streamlit as st
import mysql.connector
from database import about
from database import create_table, add_details, view_details, edit_details, del_details, attendance

def main():
    st.title("Student Attendance System")
    menu = ["Attendance", "Add Details", "View Details", "Update Details", "Remove Details","Credits"]
    ch = st.sidebar.selectbox("Menu",menu)
    create_table()
    if ch == "Attendance":
        attendance()
    elif ch == "Add Details":
        add_details()
    elif ch == "View Details":
        view_details()
    elif ch == "Update Details":
        edit_details()
    elif ch == "Remove Details":
        del_details()
    else:
        about()

if __name__ == "__main__":
    main()