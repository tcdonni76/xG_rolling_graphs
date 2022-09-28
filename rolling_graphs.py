import csv

import matplotlib.pyplot as plt
import numpy as np
from highlight_text import fig_text
from mplsoccer import Bumpy, FontManager

font_normal = FontManager(("https://github.com/google/fonts/blob/main/apache/roboto/"
                           "static/Roboto-Regular.ttf?raw=true"))
font_bold = FontManager(("https://github.com/google/fonts/blob/main/apache/roboto/"
                         "static/Roboto-Medium.ttf?raw=true"))

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
                if match[0] == team and match[1]: #Adds xG if it was home
                    teams[team].append(match[3])
                if match[4] == team and match[3]: #Adds xG if it was away
                    teams[team].append(match[1])

    for team in teams.keys():
       roll_av[team] = []
       average = 0
    for team in teams:
        for index, xG in enumerate(teams[team]):
            if xG == 'a':
                roll_av[team].append(average)
            if index > 5:
                average = 0
                for n in range(index, index - 6, -1):
                    this = teams[team]
                    # print(teams[n]) Needs to be teams[team] not xG I think, xG is singular value
                    if this[n] != 'a':
                        average = average + float(this[n])
                    else:
                        index = index + 1
                average = average / 6
            else:
                average = 0
                count = 0
                while index > -1:
                    this = teams[team]
                    if this[index] != 'a':
                        average = average + float(this[index])
                        index = index - 1
                        count = count + 1
                average = average / count
            roll_av[team].append(average)

def set_manager_text_style():
    """
    This displays when the manager came in to show the effect that they had on the rolling average
    """
    # Conte 11
    plt.axvline(x=10, ymin=0.1 ,color='#222b48', linestyle='--')
    plt.text(9.7,0.5,"Conte", color='#222b48', fontfamily="Franklin Gothic Medium")

    #Ranieri 8
    plt.axvline(x=7, ymin=0.1 ,color='yellow', linestyle='--')
    plt.text(6.7,0.5,"Ranieri", color='yellow', fontfamily="Franklin Gothic Medium")

    ## Howe 12
    plt.axvline(x=10.9, ymin=0.1 ,color='white', linestyle='--')
    plt.text(10.7,0.5,"Howe", color='white', fontfamily="Franklin Gothic Medium")

    # Dean Smith 12
    plt.axvline(x=11.1, ymin=0.1 ,color='green', linestyle='--')
    plt.text(10.7,0.4,"Smith", color='green', fontfamily="Franklin Gothic Medium")

    #Gerrard 12
    plt.axvline(x=11, ymin=0.1 ,color='#76111e', linestyle='--')
    plt.text(10.7,0.6,"Gerrard", color='#76111e', fontfamily="Franklin Gothic Medium")

    #Rangnick 15
    plt.axvline(x=14, ymin=0.1 ,color='red', linestyle='--')
    plt.text(13.7,0.5,"Rangnick", color='red', fontfamily="Franklin Gothic Medium")

    #Lampard 21
    plt.axvline(x=20, ymin=0.1 ,color='blue', linestyle='--')
    plt.text(19.7,0.6,"Lampard", color='blue', fontfamily="Franklin Gothic Medium")

    #Hodgson 21
    plt.axvline(x=20.1, ymin=0.1 ,color='yellow', linestyle='--')
    plt.text(19.7,0.5,"Hodgson", color='yellow', fontfamily="Franklin Gothic Medium")


get_data_from_csv()

min_val = 999
max_val = -999

for team in roll_av:
    for av in roll_av[team]:
        if av > max_val:
            max_val = av
        if av < min_val:
            min_val = av
bumpy = Bumpy(background_color="#000000",
              rotate_xticks=90,
              line_color="#252525",
              ticklabel_size=17, label_size=30,  # ticklabel and label font-size
              # scatter_primary='D',  # marker to be used
              plot_labels=True,  # plot the labels
              alignment_yvalue=0.1,  # y label alignment
              alignment_xvalue=1,  # x label alignment
              )
x_lst = ["Game " + str(num) for num in range(1, 25)]
y_lst = np.linspace(min_val,max_val+2,5)
# y_lst = list(map(lambda x: round(x, ndigits=2), y_lst))
highlight_dict = {
    "Watford": "yellow",
    "Newcastle Utd": "white",
    "Tottenham": "#222b48",
    "Norwich City": "green",
    "Aston Villa": "#76111e",
    "Manchester Utd": "red",
    "Everton": "blue"}

fig, ax = bumpy.plot(x_list=x_lst,
                     y_list=y_lst.astype(int),
                     values=roll_av,
                     highlight_dict=highlight_dict,
                     secondary_alpha=0.2,
                     ylim=(min_val, max_val+2),
                     upside_down=True,
figsize=(20, 16),  # size of the figure
                 y_label="xG Against",
                     fontfamily="Franklin Gothic Medium")
TITLE = "'xG against' graph for sides who have sacked their manager this season"
TEAMS_TITLE = "Teams highlighted: <Watford>, <Newcastle>, <Tottenham>, <Norwich>, <Aston Villa>, <Manchester United>" \
              " and <Everton>"
# add title
fig_text(
    0.09, 0.97, TITLE, color="#F2F2F2",
    size=20, fig=fig, fontfamily="Franklin Gothic Medium")

# add title
fig_text(
    0.09, 0.94, TEAMS_TITLE, color="#F2F2F2",
    highlight_textprops=[{"color": 'yellow'}, {"color": 'white'},  {"color": '#222b48'},
                         {"color": 'green'}, {"color": '#76111e'}, {"color": 'red'},{"color": 'blue'},],
    size=15, fig=fig, fontfamily="Franklin Gothic Medium")

set_manager_text_style()

plt.show()
