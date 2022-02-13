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
def get_data_from_csv():
    with open('xG_for.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        matches = list(reader)
        for match in matches:
            for team in teams.keys():
                if match[0] == team and match[1] != '':
                    teams[team].append(match[1])
                if match[4] == team and match[3] != '':
                    teams[team].append(match[3])
        for val in teams.values():
            print(val)



get_data_from_csv()

bumpy = Bumpy(background_color="#000000",
              line_color="#252525",
              ticklabel_size=17, label_size=30,  # ticklabel and label font-size
              scatter_primary='D',  # marker to be used
              show_right=True,  # show position on the rightside
              plot_labels=True,  # plot the labels
              alignment_yvalue=0.1,  # y label alignment
              alignment_xvalue=0.065  # x label alignment
              )
x_lst = [1,2,3,4,5]
y_lst = np.linspace(1,20,20)
vals = {"Val 1": [2,3,4,2,1]}
highlight_dict = {
    "Liverpool": "crimson"}

fig, ax = bumpy.plot(x_list=x_lst,
                     y_list=y_lst,
                     values=vals,
                     highlight_dict=highlight_dict
                     )

plt.show()
