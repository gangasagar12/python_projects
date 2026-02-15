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


#  view all student
def display_all_student():
    if student_grades():
        for name , grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("no student  found/added")


#   mian function
def main():
    while True:
        print('\nStudent grades management system: ')
        print("2. Add student")
        print("2. Update Student : ")
        print("3.Delete student:  ")
        print("4. View Student: ")
        print("5. Exit")

        choice=int(input("enter your choice="))
        if choice==1:
            name=input("enter student name==")
            grade=int(input("enter student grade="))
            add_student(name,grade)
        elif choice==2:
            name=input("enter student name= ")
            grade=int(input("enter student grade="))
            update_student(name,grade)
        elif choice==3:
            name=input("enter student name=")
            delete_student(name)
        elif choice==4:
            display_all_student()
        elif choice==5:
            print("closing the program .... ")
        else:
            print("invilid choice")