import pandas as pandas

class Statisticalanalyzer:
    def __init__(self, data):
        self.data = data

    def get_recent(self):
        stats = {
            "MP" : [],
            "HP" : [],
            "Str" : [],
            "Atk" : [],
            "Def" : [],
            "Mag" : [],
            "Spr" : [],
            "Acc" : [],
            "Spd" : [],
            "Evs" : [],
        }
        for i in self.data:
            stats["MP"].append(i["Atributes"]["MP"])
            stats["HP"].append(i["Atributes"]["HP"])
            stats["Str"].append(i["Atributes"]["Str"])
            stats["Atk"].append(i["Atributes"]["Atk"])
            stats["Def"].append(i["Atributes"]["Def"])
            stats["Mag"].append(i["Atributes"]["Mag"])
            stats["Spr"].append(i["Atributes"]["Spr"])
            stats["Acc"].append(i["Atributes"]["Acc"])
            stats["Spd"].append(i["Atributes"]["Spd"])
            stats["Evs"].append(i["Atributes"]["Evs"])
        # return the list of stats
        return stats
        
    
    def find_maximum(self):
        stats = self.get_recent()
        # uses pandas maximum method
        df = pandas.DataFrame(stats)
        # return max for each stat
        return [df["MP"].max(), df["HP"].max(), df["Str"].max(), df["Atk"].max(), df["Def"].max(), df["Mag"].max(), df["Spr"].max(), df["Acc"].max(), df["Spd"].max(), df["Evs"].max()] 

    def find_minimum(self):
        stats = self.get_recent()
        # uses pandas minimum method
        df = pandas.DataFrame(stats)
        return [df["MP"].min(), df["HP"].min(), df["Str"].min(), df["Atk"].min(), df["Def"].min(), df["Mag"].min(), df["Spr"].min(), df["Acc"].min(), df["Spd"].min(), df["Evs"].min()]
    
    def find_mean(self):
        stats = self.get_recent()
        # uses pandas mean method
        df = pandas.DataFrame(stats)
        return [df["MP"].mean(), df["HP"].mean(), df["Str"].mean(), df["Atk"].mean(), df["Def"].mean(), df["Mag"].mean(), df["Spr"].mean(), df["Acc"].mean(), df["Spd"].mean(), df["Evs"].mean()]

    def find_median(self):
        stats = self.get_recent()
        # uses pandas median method
        df = pandas.DataFrame(stats)
        return [df["MP"].median(), df["HP"].median(), df["Str"].median(), df["Atk"].median(), df["Def"].median(), df["Mag"].median(), df["Spr"].median(), df["Acc"].median(), df["Spd"].median(), df["Evs"].median()]

    def generate_report(self):
        stats = self.get_recent()
        # loops over given character list and prints out each character with their stats
        df = pandas.DataFrame(stats)
        print(df)
        # finds the minimum, maximum, median, and mean for the stats of all the characters and prints it at the bottom of the report
        maximums = self.find_maximum()
        minimums = self.find_minimum()
        means = self.find_mean()
        medians = self.find_median()
        print(f"Maximums: MP: {maximums[0]}, HP: {maximums[1]}, Str: {maximums[2]}, Atk: {maximums[3]}, Def: {maximums[4]}, Mag: {maximums[5]}, Spr: {maximums[6]}, Acc: {maximums[7]}, Spd: {maximums[8]}, Evs: {maximums[9]}")
        print(f"Minimums: MP: {minimums[0]}, HP: {minimums[1]}, Str: {minimums[2]}, Atk: {minimums[3]}, Def: {minimums[4]}, Mag: {minimums[5]}, Spr: {minimums[6]}, Acc: {minimums[7]}, Spd: {minimums[8]}, Evs: {minimums[9]}")
        print(f"Means: MP: {means[0]}, HP: {means[1]}, Str: {means[2]}, Atk: {means[3]}, Def: {means[4]}, Mag: {means[5]}, Spr: {means[6]}, Acc: {means[7]}, Spd: {means[8]}, Evs: {means[9]}")
        print(f"Medians: MP: {medians[0]}, HP: {medians[1]}, Str: {medians[2]}, Atk: {medians[3]}, Def: {medians[4]}, Mag: {medians[5]}, Spr: {medians[6]}, Acc: {medians[7]}, Spd: {medians[8]}, Evs: {medians[9]}")