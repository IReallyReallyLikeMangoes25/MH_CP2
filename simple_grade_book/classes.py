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

    def to_dict(self):
          return{"name" : self.name, "ID number" : self.id, "average" : self.average, "letter grade" : self.letter, "grade entries" : self.entries, "acedemic standig" : self.standinhg, "year" : self.year}

# gradebook class
