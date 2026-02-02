# MH 1st reading files notes
import csv
while True:
    try:
        with open("notes/reading.txt", "r") as file:
            for line in file:
                print(line.strip())
    except:
        print("That file is evil.")
    else:
        print("Huzzah!")
        break

try:
    with open("notes/Class CSV sample - Sheet1.csv", mode = "r") as csv_file:
        content = csv.reader(csv_file)
        headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0] : line[0], headers[1] : line[1]})
except:
    print("Like are files even real bro?")
else:
    for line in rows:
        print(line)
    print("Like dude, they so are.")