from time import sleep
from gun import Gun
from target import Target
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import numpy as np

status = 0
simulation_loop_time = 0.01
trajectory = np.empty([3, 0])
target = Target(25000, 0, 30000, 50, 5, 20)
gun = Gun(950, 77, 50, 10, 0)

"""
zapis lotu pocisku musi być w formie tablicy 3d
gdzie każda kalumna jest kolejną iterqacją
x 1 2 3
y 1 2 3
z 1 2 3
potrzeba jest funkcja która w interwale bedzie odcyztywać itetator ww. wektora
"""


def shoot(time, vector):
    ax.plot(0, 0, 0, "x", zdir="y")  # debug GUN
    ax.plot(target.x, target.y, target.z, "X", zdir="y")   # debug TARGET
    while True:
        shell = gun.get_shell_vector(time)
        status = target.check_hit(shell)
        ax.plot(shell[0], shell[1], shell[2], ",", zdir="y")   # debug SHELL TRAJECTORY SIMPLE
        vectors = np.array([[shell[0]], [shell[1]], [shell[2]]])
        vector = np.append(vector, vectors, 1)
        if status == 1:
            print("Target destroyed!!!!")
            break
        elif status == 2:
            print("Target missed!!!!")
            break
        else:
            # sleep(simulation_loop_time)
            time += simulation_loop_time
            continue
    return vector


fig = plt.figure()
ax = p3.Axes3D(fig)

ax.set_xlim3d([-500, 35000])
ax.set_xlabel('X')

ax.set_ylim3d([-500, 35000])
ax.set_ylabel('Y')

ax.set_zlim3d([0, 2500])
ax.set_zlabel('Z')

ax.set_title('3D Test')

data = shoot(time=0, vector=trajectory)   # [0] = x, [1] = y, [2] = z
line = [ax.plot(dat[0], dat[1], dat[2], zdir="y") for dat in data.T]   # shell trajectory vectors
# lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
# print(lines)
# print(animate_trajectory(1, data, lines))
# frames = trajectory.size
# ani = animation.FuncAnimation(fig, animate_trajectory, frames, fargs=(data, line))
#
plt.show()
