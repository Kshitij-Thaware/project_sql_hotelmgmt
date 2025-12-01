
# Function to insert dummy data
def insert_dummy_data(conn):
    cursor = conn.cursor()

    # Insert sample rooms
    cursor.execute("""
        INSERT INTO rooms (room_type, rate) VALUES
        ('Single', 50.00),
        ('Double', 80.00),
        ('Suite', 120.00)
    """)

    # Insert sample guests
    cursor.execute("""
        INSERT INTO guests (name, email, phone_number) VALUES
        ('John Doe', 'john.doe@example.com', '123-456-7890'),
        ('Jane Smith', 'jane.smith@example.com', '987-654-3210'),
        ('Michael Johnson', 'michael.johnson@example.com', '456-789-0123')
    """)

    # Insert sample reservations
    cursor.execute("""
        INSERT INTO reservations (room_number, guest_id, check_in, check_out) VALUES
        (1, 1, '2024-03-01', '2024-03-05'),
        (2, 2, '2024-03-02', '2024-03-06'),
        (3, 3, '2024-03-03', '2024-03-07')
    """)

    conn.commit()
    cursor.close()