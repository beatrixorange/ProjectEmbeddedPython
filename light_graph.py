import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
Lichtintensiteit per 60 seconden
"""

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def animate(i, xs, ys):

    # Lees de lichtintensiteit
    licht = ...

    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(licht)

    # Niet meer dan 20 waarden tegelijk in beeld
    xs = xs[-20:]
    ys = ys[-20:]

    ax.clear()
    ax.plot(xs, ys)

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.ylabel('Lichtintensiteit')

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=40000)  # delay = 60000ms = 60 sec
plt.show()
