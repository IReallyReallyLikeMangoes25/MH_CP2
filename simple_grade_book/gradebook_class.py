# mh 1st gradebook class

class gradebook:
    def __init__(self, students):
        self.students = students
        
    # search by grade, takes in students:
    def search_grade(self)
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
    def search_name(self)
        count = 1
        students_with_name = []
        # asks what name they are searching for
        name = input("What is the name of the student you are searching for: ")
        # loops through all students and if a student has that name add them to a list
        for student in self.students:
            if student.name == name:
                students_with_name.append(student)
        # print out the list
        for student in students_with_name:
            print(f"{count}. {student.name}")
        return students_with_name

    # view student record function:
    def view_record()
        # uses search function to find student they want to view the record of
        student_list = search_name(self)
        # asks which student from the list they would like to view the record of
        while True:
            choice = input("Which student would you like to view from the list (input their number): ")
            try:
                student = student_list[choice]
                break
            except:
                print("That is not a valid choice. Please input a number within the list given.")
        # prints students name, id, average grade, letter grade, grade entries, standing, and year
        print(f"{student.name}: {student.id}, {student.year}\nAverage grade: {student.average} {student.letter}\n{student.standing}\n{student.entries}")

    # view all students function, takes in students:
    def view_all(self):
        for student in self.students:
        # prints every student and their id, year, average grade, and letter grade
        print(f"{student.name}: {student.id}, {student.year} Average grade: {student.average} {student.letter}")