import Controller
import matplotlib.animation as animation
from temperature_graph import fig, xs, ys, animate
from light_graph import fig2, xs2, ys2, animate2
"""
Dit is de main file hier wordt het programma uitgevoerd.
"""

if __name__ == "__main__":
    app = Controller.Controller()
    #grafieken updaten
    aniA = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=60000)  # delay = 60000ms = 60 sec
    aniB = animation.FuncAnimation(fig2, animate2, fargs=(xs2, ys2), interval=60000)

    app.mainloop()
