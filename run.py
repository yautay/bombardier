from time import sleep
from gun import Gun
from target import Target
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
gun = Gun(950, 80, 50, 10, 0)

while True:
    shell = gun.get_shell_vector(time)
    status = target.check_hit(shell)
    ax.plot(shell[0], shell[2], shell[1], "bo")
    ax.plot(target.x, target.z, target.y, "X")
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

# for angle in range(0, 360):
#     ax.view_init(30, angle)
#     plt.draw()
#     plt.pause(.001)
print(gun.get_shell_vector(time))
plt.show()