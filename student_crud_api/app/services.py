from .models import Student

students = []

def add_student(data):
    id = len(students) + 1
    name = data['name']
    age = data['age']
    student = Student(id, name, age)
    students.append(student)
    return student.__dict__

def get_all_students():
    return [student.__dict__ for student in students]

def get_student_by_id(id):
    for student in students:
        if student.id == id:
            return student.__dict__
    return None

def update_student(id, data):
    for student in students:
        if student.id == id:
            student.name = data.get('name', student.name)
            student.age = data.get('age', student.age)
            return student.__dict__
    return None

def delete_student(id):
    for i, student in enumerate(students):
        if student.id == id:
            del students[i]
            return True
    return False
