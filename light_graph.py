import datetime as dt
import matplotlib.pyplot as plt
from Connection import light_list

"""
Lichtintensiteit per 60 seconden
"""

fig2 = plt.figure(figsize=(7, 6), dpi=100)
ax = fig2.add_subplot(111)
xs2 = []
ys2 = []

def animate2(i, xs2, ys2):

    licht = 0
    if (light_list.keys().__contains__('2')):
        temp = light_list['2']
        licht = temp[-1]

    # Tijd toevoegen aan x-as
    xs2.append(dt.datetime.now().strftime('%H:%M:%S'))
    # Lichtintensiteit toevoegen aan y-as
    ys2.append(licht)

    # Niet meer dan 20 waarden tegelijk in beeld
    xs2 = xs2[-20:]
    ys2 = ys2[-20:]

    ax.clear()
    ax.plot(xs2, ys2)

    ax.set_xticklabels(xs2, rotation=45, ha='right')
    fig2.subplots_adjust(bottom=0.30)
    ax.set_ylabel('Lichtintensiteit')