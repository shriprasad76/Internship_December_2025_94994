import mysql.connector
from mysql.connector import errorcode

# --- Database Connection Details ---
# Update these details with your actual MySQL server information
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "maneger" # Use your actual password here
DB_NAME = "sunbeam_project"

def get_connection():
    """Establishes and returns a database connection."""
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        use_pure=True
    )

def ensure_user_and_course_exist(cursor, email, course_id):
    """
    Checks if a user and a course exist. Inserts them if they don't, 
    to satisfy foreign key constraints.
    """
    # 1. Check/Insert User Email
    cursor.execute("SELECT email FROM users WHERE email = %s", (email,))
    if not cursor.fetchone():
        print(f"--> Email '{email}' not found in 'users' table. Inserting user first.")
        # NOTE: Your 'users' table might require more fields like a 'name' or 'password'.
        # If so, modify the query below to include required fields.
        insert_user_query = "INSERT INTO users (email) VALUES (%s)"
        cursor.execute(insert_user_query, (email,))
        print("--> User inserted into 'users' table.")

    # 2. Check/Insert Course ID
    cursor.execute("SELECT course_id FROM courses WHERE course_id = %s", (course_id,))
    if not cursor.fetchone():
        print(f"--> Course ID '{course_id}' not found in 'courses' table. Inserting course first.")
        # NOTE: Your 'courses' table requires 'course_name' and 'fees' (NO NULLs).
        # You must provide realistic defaults or pass these values into the function.
        # This uses defaults for demonstration.
        insert_course_query = """
        INSERT INTO courses (course_id, course_name, fees, discription, start_date) 
        VALUES (%s, %s, %s, %s, %s)
        """
        course_values = (course_id, f"Course Title {course_id}", 5000, "Default description", "2025-12-01")
        cursor.execute(insert_course_query, course_values)
        print("--> Course inserted into 'courses' table.")

def insert_student(name, email, course_id, mobile_no, profile_pic):
    """
    Manages the connection and transaction to insert a student record.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection() 
        cursor = conn.cursor()
        
        # Ensure foreign keys are valid before the main insert
        ensure_user_and_course_exist(cursor, email, course_id)

        # --- Main Insert into the 'student' table ---
        student_query = "INSERT INTO student (name, email, course_id, mobail_no, profile_pic) VALUES (%s, %s, %s, %s, %s)"
        student_values = (name, email, course_id, mobile_no, profile_pic)
        
        cursor.execute(student_query, student_values)

        # --- Commit the transaction ---
        conn.commit()
        print(f"\nSUCCESS: Record for {name} inserted successfully into 'student' table.")
        print(f"New student registration ID: {cursor.lastrowid}")

    except mysql.connector.Error as err:
        if conn:
            conn.rollback() # Rollback changes if anything fails
        print(f"\nAn error occurred during insertion: {err}")
        # Detailed error handling can be expanded here

    finally:
        # --- Clean up resources ---
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
            print("\nMySQL connection closed.")

# --- Run the function with your desired data ---
if __name__ == "__main__":
    # The script will now automatically ensure that 'shri@123' email and '123' course_id exist
    insert_student('shri', 'shri@123', 123, 1234567890, None)
