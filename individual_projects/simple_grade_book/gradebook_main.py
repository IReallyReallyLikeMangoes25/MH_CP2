# MH 1st simple grade book main
from simple_grade_book.gradebook_class import *
from simple_grade_book.student_class import *
from simple_grade_book.csv_management import *

def main():
    print("Welcome to Mirai's gradebook, for listed choice please input a number.")
    # define gradebook
    students = load_csv()
    gradebook = Gradebook()
    for student in students:
        student = Student(student["name"], student["id number"], float(student["average grade"]), student["letter grade"], student["standing"], student["year"], float(student["math"]), float(student["science"]), float(student["history"]), float(student["pe"]), float(student["elective one"]), float(student["elective two"]))
        gradebook.students.append(student)
    # WHILE loop
    while True:
        # prints user options: add student, add grade entry, view all students, view student record, view class average, and quit
        choice = input("What would you like to do:\n1. Add Student\n2. Update Grade\n3. View All Students\n4. View Student Record\n5. View Class Average\n6. Update Student's Year\n7. Quit\n")
        # if the user wants to add a student create a new student object
        if choice == "1":
            name = input("What is the new students name: ")
            id_number = input("What is the new students ID number: ")
            name = Student(name, id_number)
            gradebook.add_student(name)
        # if the user wants to enter a grade run the search function and the enter grade function
        elif choice == "2":
            if len(gradebook.students) == 0:
                print("You have no students in your gradebook yet, add a student first.")
                continue
            else:
                name = gradebook.search_name()
                name.update_grade()
        # if the user wants to view all students run the view all function
        elif choice == "3":
            if len(gradebook.students) == 0:
                print("You have no students in your gradebook yet, add a student first.")
                continue
            else:
                gradebook.view_all()
        # if the user wants to view a students record, run the view record function
        elif choice == "4":
            if len(gradebook.students) == 0:
                print("You have no students in your gradebook yet, add a student first.")
                continue
            else:
                gradebook.view_record()
        # if the user wants to view the class average run the view class average function
        elif choice == "5":
            if len(gradebook.students) == 0:
                print("You have no students in your gradebook yet, add a student first.")
                continue
            else:
                gradebook.class_summary()
        # if the user wants to quit stop running the program
        elif choice == "6":
            student = gradebook.search_name()
            student.register_year()
        elif choice == "7":
            people = []
            for person in gradebook.students:
                person = person.to_dict()
                people.append(person)
                save_csv(people)
            print("Thank you for using Mirai's gradebook!")
            break
        else:
            print("That is not an option. Please input a number given.")
            continue

#main()