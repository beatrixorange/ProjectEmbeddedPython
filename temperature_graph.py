import datetime as dt
import matplotlib.pyplot as plt
from Connection import temperature_list

"""
Temperatuur per 60 seconden
"""

fig = plt.figure(1, figsize=(7, 6), dpi=100)
ax = fig.add_subplot(111)
xs = []
ys = []

def animate(i, xs, ys):

    temp_c = 0
    if (temperature_list.keys().__contains__('1')):
        temp = temperature_list['1']
        temp_c = temp[-1]

    # Tijd toevoegen aan x-as
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))

    # Temperatuur toevoegen aan y-as
    ys.append(temp_c)

    # Niet meer dan 20 waarden tegelijk in beeld
    xs = xs[-20:]
    ys = ys[-20:]

    ax.clear()
    ax.plot(xs, ys)

    ax.set_xticklabels(xs, rotation=45, ha='right')
    fig.subplots_adjust(bottom=0.30)
    ax.set_ylabel('Temperatuur (°C)')
