from psycopg2 import sql
import streamlit as st
import logging

logging.info('Application started importing packages')
from services.connect import connect
from services.create_tables import create_tables
from services.insert import insert_guest, insert_room
from services.insert_dummy_data import insert_dummy_data
logging.info('Finished importing packages')


conn = connect() # call function to connect to db

if conn is None: #if connection fails to db
    logging.info('database connection failed')
    st.write('database connection failed')  #message prints 

else:
    # create data
    st.subheader("Create tables")
    if st.button("Add tables"):
        create_tables(conn)
        insert_dummy_data(conn)
        st.success("Tables added successfully!")


    st.title("Hotel Management System")

    # Insert data into rooms table
    st.subheader("Insert Room")
    room_type = st.selectbox("Room Type", ["Single", "Double"])
    rate = st.number_input("Rate")
    if st.button("Add Room"):
        insert_room(conn, room_type, rate)
        st.success("Room added successfully!")

    # Insert data into guests table
    st.subheader("Insert Guest")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone_number = st.text_input("Phone Number")
    if st.button("Add Guest"):
        insert_guest(conn, name, email, phone_number)
        st.success("Guest added successfully!")

    # Close the database connection
    conn.close()

