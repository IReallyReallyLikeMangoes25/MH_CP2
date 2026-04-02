# MH 1st csv management 
import csv
# load csv function:
def load_csv():
    # opens csv and loops over each line, saving it as a dictionary
    with open("simple_grade_book/students.csv", "r") as student_csv:
        content = csv.reader(student_csv)
        row_count = sum(1 for row in content)
        student_csv.seek(0)
        if row_count == 0:
            headers = ["name", "id number", "average grade", "letter grade", "standing", "year", "math", "science", "history", "pe", "elective one", "elective two"]
        else:
            headers = next(content)
        rows = []
        for line in content:
            # saves all the dictionaries of lines in a list
            rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2], headers[3] : line[3],headers[4] : line[4], headers[5] : line[5], headers[6] : line[6], headers[7] : line[7],headers[8] : line[8], headers[9] : line[9], headers[10] : line[10], headers[11] : line[11]})
        return rows
    
def save_csv(students):
    fieldnames = ["name", "id number", "average grade", "letter grade", "standing", "year", "math", "science", "history", "pe", "elective one", "elective two"]
    # loops over csv and dictionary changing every line of the csv to be the same as in the dictionary.
    with open("simple_grade_book/students.csv", "w", newline = "") as student_csv:
        writer = csv.DictWriter(student_csv, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(students)
