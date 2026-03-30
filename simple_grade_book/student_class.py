# mh 1st simple grade book classes

# student class
class student:
    # defines name, id number, average grade and letter grade, grade entries, academic standing, and year
    def __init__(self, name, id, average, letter, entries, standing, year):
            self.name = name
            self.id = id
            self.average = average
            self.letter = letter
            self.entries = entries
            self.standing = standing
            self.year = year

    def to_str(self):
          return f"{self.name}: {self.id}, {self.year}\nAverage grade: {self.average} {self.letter}\n{self.standing}"
    
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
        for grade in grades.values:
            if int(self.average) >= grade:
                  self.letter = grade.key
                  break
            else:
                  self.letter = "F"

    
    def calculate_average(self):
        # calculate average:
        # loops over all grade entries and adds them together, adding one to the total count for each
        # divides added grades by amount of grades
        total = 0
        count = 0
        for grade in self.entries:
              total += grade
              count += 1
        average_grade = total/count
        self.average = average_grade
    
    def add_grade(self):
        # add grade function:
        # asks what grade they want to add
        while True:
                grade = input("Type in the grade you want to add: ")
                if grade.isinstance == False:
                        print("Please input a number")
                        continue
                else:
                        break
        # adds that grade to the students grades
        self.entries.append(grade)
        # calculates new average and letter grade
        self.calculate_average(self)
        self.letter_grade(self)
        self.acedemic_standing(self)
