# initialized dictionary
student_grades={ }

#  add  new student
def add_student(name,grade):
    student_grades[name]=grade
    print(f"added{name} with a {grade}")

#update a student
def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade

        print(f"{name} with marks are  updated{grade}")
    else:
        print(f"{name} is not found!")

#delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]   
        print(f"{name} has been sucessfully deleted:")
    else:
        print(f"{name} is not found!")