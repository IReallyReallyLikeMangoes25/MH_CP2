# mh 1st csv management file
import csv
import pandas as pd
import json

def load_csv():
    # loops over csv and saves every line in a dictionary
    # saves all dictionaries in a list
    # returns the list
    with open("individual_projects/update_character_manager/characters.csv", "r") as characters:
        content = csv.reader(characters)
        row_count = sum(1 for row in content)
        characters.seek(0)
        if row_count == 0:
            headers = ["name","race","class","level","attack","defense","magic","speed","health","item slot 1","item slot 2","item slot 3","item slot 4","weapon","armor", "backstory", "quest", "quest", "description", "trait 1", "trait 2", "trait 3"]
        else:
            headers = next(content)
        rows = []
        for line in content:
                rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2], headers[3] : line[3],headers[4] : line[4], headers[5] : line[5], headers[6] : line[6], headers[7] : line[7],headers[8] : line[8], headers[9] : line[9], headers[10] : line[10], headers[11] : line[11], headers[12] : line[12], headers[13] : line[13], headers[14] : line[14], headers[15] : line[15], headers[16] : line[16], headers[17] : line[17], headers[18] : line[18], headers[19] : line[19], headers[20] : line[20]})
        return rows


def save_csv(data):
    # loops over the data and adds it line by line to the csv
    fieldnames = ["name","race","class","level","attack","defense","magic","speed","health","item slot 1","item slot 2","item slot 3","item slot 4","weapon","armor", "backstory", "quest", "quest", "description", "trait 1", "trait 2", "trait 3"]
    # loops over csv and dictionary changing every line of the csv to be the same as in the dictionary.
    with open("individual_projects/update_character_manager/characters.csv", "w", newline = "") as characters:
        writer = csv.DictWriter(characters, fieldnames = fieldnames)
        writer.writeheader()
        print(data)
        #writer.writerows(data)

def backup_csv(data):
    # loops over the data and adds it line by line to the csv, then saves it as a backup
    fieldnames = ["name","race","class","level","attack","defense","magic","speed","health","item slot 1","item slot 2","item slot 3","item slot 4","weapon","armor", "backstory", "quest", "quest", "description", "trait 1", "trait 2", "trait 3"]
    # loops over csv and dictionary changing every line of the csv to be the same as in the dictionary.
    with open("individual_projects/update_character_manager/characters.csv", "w", newline = "") as characters:
        writer = csv.DictWriter(characters, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(data)

def load_df():
    pass
def save_df(characters):
    # converts all characters to a dataframe
    df = pd.DataFrame(characters.values(), columns = ["characters"])
    df["characters"] = df["characters"].apply(list)
    df["characters"] = df["characters"].map(json.dumps)
    # takes the character names and saves them in a csv
    df.to_csv("individual_projects\update_character_manager\characters.csv", index = False)
