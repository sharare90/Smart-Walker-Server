import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


file_name = './logs/log.txt'
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 2)
ax2 = fig.add_subplot(2, 2, 1)
ax3 = fig.add_subplot(2, 2, 4)
ax4 = fig.add_subplot(2, 2, 3)


def animate(i):
    data = np.loadtxt(file_name)
    ax1.set_title("fr")
    ax2.set_title("fl")
    ax3.set_title("rr")
    ax4.set_title("rl")
    ax1.set_ylim([-1000, 1000])
    ax2.set_ylim([-1000, 1000])
    ax3.set_ylim([-1000, 1000])
    ax4.set_ylim([-1000, 1000])
    ax1.plot(data[:, 0], color='red')
    ax2.plot(data[:, 1], color='green')
    ax3.plot(data[:, 2], color='magenta')
    ax4.plot(data[:, 3], color='blue')


ani = animation.FuncAnimation(fig, animate, interval=200)
plt.show()
