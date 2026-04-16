# mh 1st csv management file
import pandas as pd
import ast

def load_df():
    # creates data frame
    df = pd.read_csv("individual_projects/update_character_manager/characters.csv")
    char_dict = {}
    for index, row in df.iterrows():
        char_dict[row["names"]] = ast.literal_eval(row["characters"])
    return char_dict

def save_df(characters):
    # converts all characters to a dataframe
    keys = list(characters.keys())
    values = list(characters.values())
    row_data = []
    # saves characters by name
    for i in range(len(keys)):
        row_data.append([keys[i], values[i]])
    df = pd.DataFrame(row_data, columns = ["names", "characters"])
    df.to_csv("individual_projects/update_character_manager/characters.csv")