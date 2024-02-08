from flask import Blueprint
from .controllers import create_student, get_students, get_student, modify_student, remove_student

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/v1/students', methods = ['POST'])
def add_student():
    return create_student

@api_bp.route('api/v1/students', methods = ['GET'])
def list_all_students():
    return get_students()

@api_bp.route('api/v1/students/<int:id>', methods = ['GET'])
def list_one_student(id):
    return get_student(id)

@api_bp.route('api/v1/students/<int:id>', methods = ['PUT'])
def update_one_student(id):
    return modify_student(id)

@api_bp.route('api/v1/students/<int:id>', methods = ['DELETE'])
def delete_one_student(id):
    return remove_student(id)
