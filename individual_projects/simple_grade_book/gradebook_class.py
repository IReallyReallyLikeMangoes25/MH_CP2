# mh 1st gradebook class
import csv
class Gradebook:
    def __init__(self, students = []):
        self.students = students
    
    def add_student(self, student):
        self.students.append(student)
        
    def class_summary(self):
        total = 0
        count = 0
        # loops over all students and adds their grades together, then divides by the amount of students
        for student in self.students:
                total += student.average
                count += 1
        print(f"The class average is {total/count}")

    # search by grade, takes in students:
    def search_grade(self):
        letter_grades = ["A","A-","B+","B","B-","C+","C","C-","D+","D","F"]
        students_with_grade = []
        # asks what letter grade they are searching for
        while True:
            desired = input("What letter grade are you searching for: ")
            if desired not in letter_grades:
                print("That is not a letter grade.")
                continue
            else:
                break
        # loops through all students and if a student has that letter grade add them to a list
        for student in self.students:
            if student.letter == desired:
                students_with_grade.append(student.name)
        # print out the list
        for students in students_with_grade:
            print(student)

    # search by name, takes in students:
    def search_name(self):
        count = 1
        students_with_name = []
        # asks what name they are searching for
        while True:
            name = input("What is the name of the student you are searching for: ")
            # loops through all students and if a student has that name add them to a list
            for student in self.students:
                if student.name == name:
                    students_with_name.append(student)
                # print out the list
            for student in students_with_name:
                print(f"{count}. {student.name}, {student.id}")
                count += 1
            name = input("Which student from that list do you choose: ")
            try:
                name = int(name)
                name = students_with_name[name - 1]
                break
            except:
                print("Please input a number provided in the list.")

        return name

    # view student record function, takes in students:
    def view_record(self):
        # uses search function to find student they want to view the record of
        student = self.search_name()
        # prints students name, id, average grade, letter grade, grade entries, standing, and year
        print(f"{student.name}: {student.id}, {student.year}\nAverage grade: {round(student.average, 3)}, {student.letter}\n{student.standing}\nMath: {student.math}\nScience: {student.science}\nHistory: {student.history}\nPhys Ed: {student.pe}\nElective One: {student.elective_1}\nElective Two: {student.elective_2}")

    # view all students function, takes in students:
    def view_all(self):
        for student in self.students:
        # prints every student and their id, year, average grade, and letter grade
            print(f"{student.name}: {student.id}, {student.year}, Average grade: {student.average}, {student.letter}")
    
    def save_file(self):
        with open("simple_grade_book/students.csv", "w", newline = "") as student_csv:
             # sets fieldnames
            fieldnames = ["name", "id number", "average grade", "letter grade", "standing", "year", "math", "science", "history", "pe", "elective one", "elective two"]
            # loops over every student in the gradebook and adds them to the csv
            writer = csv.DictWriter(student_csv, fieldnames)
            writer.writeheader()
            for student in self.students:
                writer.writerows(vars(student))