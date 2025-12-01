# Function to insert data into rooms table
def insert_room(conn, room_type, rate):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO rooms (room_type, rate) VALUES (%s, %s)
    """, (room_type, rate))
    conn.commit()
    cursor.close()

# Function to insert data into guests table
def insert_guest(conn, name, email, phone_number):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO guests (name, email, phone_number) VALUES (%s, %s, %s)
    """, (name, email, phone_number))
    conn.commit()
    cursor.close()