import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

"""
Temperatuur per 60 seconden

interrupt staat nog op 1 sec voor testen
"""

fig = plt.figure(figsize=(7, 5), dpi=100)
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def animate(i, xs, ys):

    # Lees de temperatuur
    temp_c = random.randint(10, 30)

    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(temp_c)

    # Niet meer dan 20 waarden tegelijk in beeld
    xs = xs[-20:]
    ys = ys[-20:]

    ax.clear()
    ax.plot(xs, ys)

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.ylabel('Temperatuur (°C)')

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)  # delay = 60000ms = 60 sec
plt.show()