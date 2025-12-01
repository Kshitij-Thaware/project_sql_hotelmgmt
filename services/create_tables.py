import psycopg2
# Function to create tables
def create_tables(conn):

    try:
        cursor = conn.cursor()

        # Create rooms table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS rooms (
                room_number SERIAL PRIMARY KEY,
                room_type VARCHAR(50),
                rate DECIMAL
            )
        """)

        # Create guests table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS guests (
                guest_id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100),
                phone_number VARCHAR(15)
            )
        """)

        # Create reservations table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reservations (
                reservation_id SERIAL PRIMARY KEY,
                room_number INTEGER REFERENCES rooms(room_number),
                guest_id INTEGER REFERENCES guests(guest_id),
                check_in DATE,
                check_out DATE,
                FOREIGN KEY (room_number) REFERENCES rooms(room_number),
                FOREIGN KEY (guest_id) REFERENCES guests(guest_id)
            )
        """)

        conn.commit()
        cursor.close()
    
    except psycopg2.Error as e:
        print(f"Unable to create tables to the database: {e}")
        return None