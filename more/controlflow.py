#While else


students = []

class Student:

    school_name = "Unique Child International"
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        student = {"name":name, "student_id": student_id }
        students.append(student)

    def __str__(self):
        return f'{self.name} {self.student_id}'

    def get_name_capitalize(self):
        return self.name.capitalize()


student = Student("Desmond", 34)

print(student)
print(students)