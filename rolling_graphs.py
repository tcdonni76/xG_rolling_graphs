import json
from urllib.request import urlopen

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from highlight_text import fig_text
import csv
from mplsoccer import Bumpy, FontManager, add_image

teams = {
    "Arsenal": [],
    "Aston Villa": [],
    "Brentford": [],
    "Brighton": [],
    "Burnley": [],
    "Chelsea": [],
    "Crystal Palace": [],
    "Everton": [],
    "Leeds United": [],
    "Leicester City": [],
    "Liverpool": [],
    "Manchester City": [],
    "Manchester Utd": [],
    "Newcastle Utd": [],
    "Norwich City": [],
    "Southampton": [],
    "Tottenham": [],
    "Watford": [],
    "West Ham": [],
    "Wolves": []
}

roll_av = {}

def get_data_from_csv():
    with open('xG_for.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')    #Reads in CSV
        matches = list(reader)
        for match in matches:
            for team in teams.keys():
                if match[0] == team and match[1] != '': #Adds xG if it was home
                    teams[team].append(match[1])
                if match[4] == team and match[3] != '': #Adds xG if it was away
                    teams[team].append(match[3])

    for team in teams.keys():
       roll_av[team] = []
       print(teams[team])

    for team in teams:
        print(team)
        for index, xG in enumerate(teams[team]):
            average = 0
            print(xG)
            if index > 5:
                for n in range(index, index - 6, -1):
                    this = teams[team]
                    print(this[n])
                    # print(teams[n]) Needs to be teams[teanm] not xG I think, xG is singular value
                    average = average + float(this[n])
                average = average / 6
            else:
                count = 0
                while index > -1:
                    this = teams[team]
                    print(this[index])
                    a = this[index]
                    b = float(this[index])
                    average = average + float(this[index])
                    index = index - 1
                    count = count + 1
                average = average / count
            roll_av[team].append(average)

    for team in roll_av.keys():
        print(team)
        print(roll_av[team])

get_data_from_csv()

min_val = 999
max_val = -999

for team in roll_av:
    for av in roll_av[team]:
        if av > max_val:
            max_val = av
        if av < min_val:
            min_val = av
print(max_val)

bumpy = Bumpy(background_color="#000000",
              rotate_xticks=90,
              line_color="#252525",
              ticklabel_size=17, label_size=30,  # ticklabel and label font-size
              # scatter_primary='D',  # marker to be used
              plot_labels=True,  # plot the labels
              alignment_yvalue=0.1,  # y label alignment
              alignment_xvalue=1,  # x label alignment
              )
x_lst = ["Week " + str(num) for num in range(1, 25)]
y_lst = np.linspace(min_val,max_val+1,5)
# y_lst = list(map(lambda x: round(x, ndigits=2), y_lst))
highlight_dict = {
    "Manchester City": "skyblue",
    "Liverpool": "crimson",
    "Manchester Utd": "red",
    "Tottenham": "white",
    "West Ham": "#751c30",
    "Chelsea": "blue"}

fig, ax = bumpy.plot(x_list=x_lst,
                     y_list=y_lst.astype(int),
                     values=roll_av,
                     highlight_dict=highlight_dict,
                     upside_down=True,
                     secondary_alpha=0.3,
                     ylim=(min_val, max_val+2)
                                          )
TITLE = "'xG for' graph for selected sides, <Manchester City>, <Liverpool>, <Manchester Utd>, <Tottenham>,"
OTHER_TITLE = "<West Ham> and <Chelsea>, based on a six game rolling average"
# add subtitle
fig_text(
    0.09, 0.95, TITLE, color="#F2F2F2",
    highlight_textprops=[{"color": 'skyblue'}, {"color": 'crimson'}, {"color": 'red'}, {"color": 'white'}],
    size=15, fig=fig)

# add subtitle
fig_text(
    0.09, 0.92, OTHER_TITLE, color="#F2F2F2",
    highlight_textprops=[{"color": '#751c30'}, {"color": 'blue'}],
    size=15, fig=fig)

plt.show()
