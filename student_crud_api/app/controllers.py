from flask import jsonify, request
from .models import Student
from .services import add_student, get_all_students, get_student_by_id, delete_student, update_student

def create_student():
    data = request.get_json()
    student = add_student(data)
    return jsonify(student), 201

def get_students():
    students = get_all_students()
    return jsonify(students)

def get_student(id):
    student = get_student_by_id(id)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error" : "student not found"}), 404
    
def modify_student(id):
    data = request.get_json()
    student = update_student(id, data)
    if student:
        return jsonify(student)
    else:
        jsonify({"error" : "student not found"}), 404

def remove_student(id):
    success = delete_student(id)
    if success:
        return jsonify({"message" : "student deleted successfully"}), 200
    else:
        return jsonify({"message" : "student not found"}), 404