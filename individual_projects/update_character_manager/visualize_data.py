import matplotlib.pyplot as plt
import math

class DataVisualization:
    def __init__(self, data):
        self.data = data
    pass
    # radar graph function
    def radar_graph(self):
        titles = ["Attack", "Defense", "Magic", "Speed", "Health"]
        for character in self:
            stats = [character["attack"], character["defense"], character["magic"], character["speed"], character["health"]]
            # converts degrees to radians
            angles = angles = [math.radians(a) for a in [0, 60, 120, 180, 240, 300]]
            # adds first index of a list to the end so the polygon will close
            angles += [angles[0]]
            stats += [stats[0]]
            # create polar plot
            fig, ax = plt.subplots(subplot_kw = dict(polar = True))
            # plot the stats
            ax.plot(angles, stats, label = character["name"])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(titles)
        ax.set_title("Character Stats")
        ax.legend(loc = "upper right", bbox_to_anchor = (1, 0))
        plt.tight_layout()
        plt.show()

    # bar graph function
    def bar_graph(self):
        positions = [0, 3, 6, 9, 12]
        for character in self:
            # creates bars with height corresponding to how high the stat is for every stat
            stats = [character["attack"], character["defense"], character["magic"], character["speed"], character["health"]]
            titles = ["Attack", "Defense", "Magic", "Speed", "Health"]
            fig, ax = plt.subplots()
            ax.bar(positions, stats, label = character["name"])
            ax.set_xticks(positions)
            ax.set_xticklabels(titles)
            ax.set_title("Character Stats")
            for i in positions:
                i += 1
        ax.legend()
        plt.show()

    # line chart, takes in a character:
    def line_chart(self, list, stat_choice):
        stat = []
        # get all the instances of the chosen stat for the chosen character
        for item in list:
            if item["name"] == self["name"]:
                stat.append(item[stat_choice])
        # plots how a characters stat has changed over time
        plt.plot(stat)
        plt.xlabel("")
        plt.ylabel("")
        plt.title(f"{self["name"]}'s {stat_choice} Stat")