from flask import Blueprint, request, jsonify
from assignment2 import get_db_connection

course_bp = Blueprint("course_bp", __name__)

# GET ALL COURSES
@course_bp.route("/courses", methods=["GET"])
def get_courses():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

# GET SINGLE COURSE
@course_bp.route("/courses/<int:id>", methods=["GET"])
def get_single_course(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses WHERE course_id=%s", (id,))
    course = cursor.fetchone()
    conn.close()

    if course:
        return jsonify(course)
    return jsonify({"message": "Course not found"}), 404

# ADD COURSE
@course_bp.route("/courses", methods=["POST"])
def add_course():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO courses
    (course_name, discription, fees, start_date, end_date, vido_expire_days)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        data["course_name"],
        data["discription"],
        data["fees"],
        data["start_date"],
        data["end_date"],
        data["vido_expire_days"]
    ))

    conn.commit()
    conn.close()
    return jsonify({"message": "Course added successfully"})

# UPDATE COURSE FEES
@course_bp.route("/courses/<int:id>", methods=["PUT"])
def update_course_fees(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE courses SET fees=%s WHERE course_id=%s",
        (data["fees"], id)
    )

    conn.commit()
    conn.close()
    return jsonify({"message": "Course fees updated"})

# DELETE COURSE
@course_bp.route("/courses/<int:id>", methods=["DELETE"])
def delete_course(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE course_id=%s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Course deleted"})
