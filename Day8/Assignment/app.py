from flask import Flask, jsonify
from course_routes import course_bp
from student_routes import student_bp

app = Flask(__name__)

# HOME API
@app.route("/")
def home():
    return jsonify({"message": "Sunbeam Project API Running"})

# REGISTER BLUEPRINTS
app.register_blueprint(course_bp)
app.register_blueprint(student_bp)

# RUN SERVER
if __name__ == "__main__":
    app.run(debug=True)
