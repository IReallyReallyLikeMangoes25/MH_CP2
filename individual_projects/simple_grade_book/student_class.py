# mh 1st student class

# student class
class Student:
      # defines name, id number, average grade and letter grade, grade entries, academic standing, and year
      def __init__(self, name, id, average = 0, letter = "No letter grade yet", standing = "No standing yet", year = "No registered year yet", math = 0, science = 0, history = 0, pe = 0, elective_1 = 0, elective_2 = 0):
            self.name = name
            self.id = id
            self.average = average
            self.letter = letter
            self.standing = standing
            self.year = year
            self.math = math
            self.science = science
            self.history = history
            self.pe = pe
            self.elective_1 = elective_1
            self.elective_2 = elective_2

      def to_dict(self):
            return {"name" : self.name, "id number" : self.id, "average grade" : self.average, "letter grade" : self.letter, "standing" : self.standing, "year" : self.year, "math" : self.math, "science" : self.science, "history" : self.history, "pe" : self.pe, "elective one" : self.elective_1, "elective two" : self.elective_2}
      
      def register_year(self):
            # register year function:
            years = ["9th", "10th", "11th", "12th"]
            count = 1
            # prints out possible years
            for year in years:
                  print(f"{count}. {year}")
                  count += 1
            # asks user which the student is
            while True:
                  choice = input("What year is this student: ")
                  try:
                        choice = int(choice)
                        choice = years[choice - 1]
                        break
                  except:
                        print("PLease input a number in the given list.")
            # changes students year
            self.year = choice

      def acedemic_standing(self):
            # acedemic standing function:
            # if the letter grade is A or A- return "Honor roll"
            if self.letter == "A" or self.letter == "A-":
                  self.standing = "Honor Roll"
            # if the letter grade is B+, B, or B- return "Good standing"
            elif self.letter == "B+" or self.letter == "B" or self.letter == "B-":
                  self.standing = "Good Standing"
            # otherwise return "needs improvement
            else:
                  self.standing = "Needs Improvement"
      
      def letter_grade(self):
            # letter grade function:
            # save all grades in a dictionary, with a list of numbers of what they could be
            grades = {"A" : 94, "A-" : 90, "B+" : 87, "B" : 83, "B-" : 80, "C+" : 77, "C" : 73, "C-" : 70, "D+" : 67, "D" : 60}
            # loops over each grade and if the students average is in range return the corresponding letter grade
            for key, value in grades.items():
                  if int(self.average) >= value:
                        self.letter = key
                        break
                  else:
                        self.letter = "F"

      
      def calculate_average(self):
            # calculate average:
            # divides all grades by amount of classes
            count = 6
            total = self.math + self.science + self.history + self.pe + self.elective_1 + self.elective_2
            average_grade = total/count
            self.average = average_grade
      
      def update_grade(self):
            # add grade function:
            count = 1
            classes = ["Math", "Science", "History", "Phys Ed", "First Elective", "Second Elective"]
            # print out all class options and chooses which class they want to update the grade for
            for cls in classes:
                  print(f"{count}. {cls}")
                  count += 1
            while True:
                  choice = input("What class do you want to update the grade for: ")
                  try:
                        choice = int(choice)
                        choice = classes[choice - 1]
                        break
                  except:
                        print("Please input a number in the given list.")
                  # asks what grade they want to add
            while True:
                  grade = input(f"What should be added to this students {choice} grade: ")
                  try:   
                        grade = float(grade)
                        break
                  except:
                        print("Please input a number.")
                        continue
            # adds that grade to the students grades
            if choice == "Math":
                  self.math += grade
            elif choice == "Science":
                  self.science += grade
            elif choice == "History":
                  self.history += grade
            elif choice == "Phys Ed":
                  self.pe += grade
            elif choice == "First Elective":
                  self.elective_1 += grade
            elif choice == "Second Elective":
                  self.elective_2 += grade
            # calculates new average and letter grade
            self.calculate_average()
            self.letter_grade()
            self.acedemic_standing()

