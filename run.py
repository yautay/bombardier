from time import sleep
from gun import Gun
from target import Target
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Setting the axes properties
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlim3d([-50000, 50000])
ax.set_xlabel('X')

ax.set_ylim3d([-50000, 50000])
ax.set_ylabel('Y')

ax.set_zlim3d([0, 5000])
ax.set_zlabel('Z')

ax.set_title('3D Test')


status = 0
time = 0
simulation_loop_time = 0.01

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

trajectory = np.empty([3, 0])

def shoot(time, trajectory):
    ax.plot(target.x, target.z, target.y, "X")
    while True:
        shell = gun.get_shell_vector(time)
        status = target.check_hit(shell)
        ax.plot(shell[0], shell[2], shell[1], ",")
        vectors = np.array([[shell[0]], [shell[2]], [shell[1]]])
        trajectory = np.append(trajectory, vectors, 1)
        if status == 1:
            print("Target destroyed!!!!")
            print(time)
            print(shell)
            print(target.coordinates)
            break
        elif status == 2:
            print(time)
            print("Target missed!!!!")
            break
        else:
            # sleep(simulation_loop_time)
            time += simulation_loop_time
            continue
    return trajectory


trajectory = shoot(time, trajectory)
print(trajectory.size)
print(gun.get_shell_vector(time))

plt.show()
