from gun import Gun
from target import Target
from wind import Wind
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

target = Target(x=19028, y=-50, z=10800, l=250, h=50, w=32, sog=0, cog=0)
gun = Gun(vm=400, alpha=45, gamma=0, l=10, yb=0, m=50, cd=30, sim="simple")
wind = Wind(velocity=0, gamma=30)


data = gun.shoot(target=target, loop_interval=0.5, wind=wind)   # [0] = x, [1] = y, [2] = z


def animate_trajectory(num, data_set, path):
    path.set_data(data_set[:2, :num])
    path.set_3d_properties(data_set[2, :num], zdir="y")
    return path


fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlim3d([-500, 35000])
ax.set_xlabel('X')
ax.set_ylim3d([-500, 15000])
ax.set_ylabel('Z')
ax.set_zlim3d([0, 2500])
ax.set_zlabel('Y')

line = plt.plot(data[0], data[1], data[2], zdir="y", lw=2, c="g")[0]   # shell trajectory vectors
frames = len(data.T)


shell_animation = animation.FuncAnimation(fig, animate_trajectory, frames=frames, fargs=(data, line), interval=15, blit=False)
shell_animation.save("shot_test.mp4")

plt.show()