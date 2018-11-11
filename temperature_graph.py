import datetime as dt
import matplotlib.pyplot as plt
import random

"""
Temperatuur per 60 seconden

interrupt staat nog op 1 sec voor testen
"""

fig = plt.figure(1, figsize=(7, 5), dpi=100)
ax = fig.add_subplot(111)
xs = []
ys = []

def animate(i, xs, ys):

    # TODO Hier moet de temperatuur gelezen worden
    temp_c = random.randint(10, 30)

    # Tijd toevoegen aan x-as
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    # Temperatuur toevoegen aan y-as
    ys.append(temp_c)

    # Niet meer dan 7 waarden tegelijk in beeld
    xs = xs[-7:]
    ys = ys[-7:]

    ax.clear()
    ax.plot(xs, ys)

    ax.set_xticklabels(xs, rotation=45, ha='right')
    fig.subplots_adjust(bottom=0.30)
    ax.set_ylabel('Temperatuur (°C)')
