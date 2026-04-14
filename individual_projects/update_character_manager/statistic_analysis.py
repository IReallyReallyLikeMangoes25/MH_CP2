import pandas as pandas

class Statisticalanalyzer:
    def __init__(self, data):
        self.data = data

    def get_recent(self):
        last = self[0]
        recent = []
        stats = []
        # loops over the data
        for character in self:
            # if the name is the same as the last one checked, move on
            if character["name"] == last["name"]:
                last = character
                continue
            # if the last name checked is not the same as the current name, add the last name checked to the recent list and move on
            else:
                recent.append(last)
                last = character
                continue
        # from the recent list, pull all the stats and add them to their own list
        for character in recent:
            stats.append(character["attack"])
            stats.append(character["deffense"])
            stats.append(character["magic"])
            stats.append(character["speed"])
            stats.append(character["health"])
        # return the list of stats
        return stats, recent
        
    
    def find_maximum(self):
        stats, recent = self.get_recent()
        # uses pandas maximum method
        df = pandas.DataFrame(stats)
        return df.max()

    def find_minimum(self):
        stats, recent = self.get_recent()
        # uses pandas minimum method
        df = pandas.DataFrame(stats)
        return df.min()
    
    def find_mean(self):
        stats, recent = self.get_recent()
        # uses pandas mean method
        df = pandas.DataFrame(stats)
        return df.mean()

    def find_median(self):
        stats, recent = self.get_recent()
        # uses pandas median method
        df = pandas.DataFrame(stats)
        return df.median()

    def generate_report(self):
        stats, recent = self.get_recent()
        # loops over given character list and prints out each character with their stats
        df = pandas.DataFrame(recent)
        print(df)
        # finds the minimum, maximum, median, and mean for the stats of all the characters and prints it at the bottom of the report
        print(f"Maximum: {stats.find_maximum()}")
        print(f"Minimum:{stats.find_minimum()}")
        print(f"Mean: {stats.find_mean()}")
        print(f"Median: {stats.find_median()}")