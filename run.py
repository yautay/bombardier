from time import sleep
from gun import Gun
from target import Target
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import numpy as np

status = 0
simulation_loop_time = 0.05
trajectory = np.empty([3, 0])
target = Target(25000, 0, 30000, 50, 5, 20)
gun = Gun(700, 77, 30, 10, 0)

"""
zapis lotu pocisku musi być w formie tablicy 3d
gdzie każda kalumna jest kolejną iterqacją
x 1 2 3
y 1 2 3
z 1 2 3
potrzeba jest funkcja która w interwale bedzie odcyztywać itetator ww. wektora
"""


def shoot(time, vector):
    while True:
        shell = gun.get_shell_vector(time)
        status = target.check_hit(shell)
        vectors = np.array([[shell[0]], [shell[1]], [shell[2]]])
        vector = np.append(vector, vectors, 1)
        if status == 1:
            print("Target destroyed!!!!")
            break
        elif status == 2:
            print("Target missed!!!!")
            break
        else:
            time += simulation_loop_time
            continue
    return vector


def animate_trajectory(num, data_set, path):
    path.set_data(data_set[:2, :num])
    path.set_3d_properties(data_set[2, :num], zdir="y")
    # print(path)
    return path


data = shoot(time=0, vector=trajectory)   # [0] = x, [1] = y, [2] = z

fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlim3d([-500, 35000])
ax.set_xlabel('X')

ax.set_ylim3d([-500, 35000])
ax.set_ylabel('Z')

ax.set_zlim3d([0, 2500])
ax.set_zlabel('Y')

ax.set_title('3D Test')

line = plt.plot(data[0], data[1], data[2], zdir="y", lw=2, c="g")[0]   # shell trajectory vectors
frames = len(data.T)

shell_animation = animation.FuncAnimation(fig, animate_trajectory, frames=frames, fargs=(data, line), interval=15, blit=False)
shell_animation.save("shot_test.mp4")
plt.show()
