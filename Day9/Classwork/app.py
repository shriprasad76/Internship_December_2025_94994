from flask import Flask, jsonify
app=Flask(__name__)
def create_result(error,data):
    if data:
        return jsonify(status="duccess",data=data)
    else

@app.get("/api1")
def api1():
    return jsonify(message="hello , world!")

@app.get("/api2")
def api2():
