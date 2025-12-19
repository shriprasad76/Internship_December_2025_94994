from flask import Blueprint, request, jsonify
from assignment2 import get_db_connection

student_bp = Blueprint("student_bp", __name__)

# GET ALL STUDENTS
@student_bp.route("/students", methods=["GET"])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

# ADD STUDENT
@student_bp.route("/students", methods=["POST"])
def add_student():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO student
    (name, email, course_id, mobail_no)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (
        data["name"],
        data["email"],
        data["course_id"],
        data["mobail_no"]
    ))

    conn.commit()
    conn.close()
    return jsonify({"message": "Student added successfully"})

# UPDATE STUDENT MOBILE
@student_bp.route("/students/<int:id>", methods=["PUT"])
def update_student_mobile(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE student SET mobail_no=%s WHERE reg_no=%s",
        (data["mobail_no"], id)
    )

    conn.commit()
    conn.close()
    return jsonify({"message": "Student mobile updated"})

# DELETE STUDENT
@student_bp.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE reg_no=%s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Student deleted"})
