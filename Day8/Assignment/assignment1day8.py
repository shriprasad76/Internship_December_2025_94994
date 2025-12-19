import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="maneger",
        database="sunbeam_project",
        use_pure=True
    )
    return connection

def portal_operations():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        print("Connected to sunbeam_project database successfully.\n")

        user_email = 'rahul@example.com'
        cursor.execute(
            "INSERT INTO users (email, password, role) VALUES (%s, %s, %s)", 
            (user_email, 'securepassword123', 'student')
        )
        print(f"User {user_email} added to users table.")

        cursor.execute("INSERT INTO courses (course_name, fees) VALUES ('Web Tech', 12000)")
        new_course_id = cursor.lastrowid 
        print(f"New Course 'Web Tech' created with ID: {new_course_id}")

        cursor.execute(
            "INSERT INTO student (name, email, mobail_no, course_id) VALUES (%s, %s, %s, %s)", 
            ('Rahul', user_email, '9890001122', new_course_id) 
        )
        conn.commit()
        print("Student records inserted successfully.")

        for table in ["users", "courses", "student"]:
            print(f"\n--- Current {table.upper()} Records ---")
            cursor.execute(f"SELECT * FROM {table}")
            for row in cursor.fetchall(): print(row)
            
        cursor.execute("DELETE FROM student WHERE email = %s", (user_email,))
        cursor.execute("DELETE FROM users WHERE email = %s", (user_email,))
  
        cursor.execute("DELETE FROM courses WHERE course_id = %s", (new_course_id,))
        conn.commit()
        print(f"\nRecords associated with {user_email} and course {new_course_id} deleted for cleanup.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    portal_operations()
