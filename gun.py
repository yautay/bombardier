from target import Target
from wind import Wind
import math
import numpy as np


class Gun:
    def __init__(self, vm, alpha, gamma, l, yb, m = None, cd = None, sim = "simple"):
        self.__sim = sim   # simple -> no drag & no wind taken into consideration
        self.__mass = m   # projectile mass
        self.__drag_coff = cd   # projectile drag coefficient
        self.__vm = vm   # muzzle velocity m/s
        self.__alpha = alpha   # vertical inclination
        self.__gamma = gamma   # horizontal azimuth
        self.__l = l   # barrel length
        self.__yb = yb   # gun elevation
        self.__dir_cos = self.__get_angle_cos()
        self.__barrel_coordinates = self.__get_barrel_coordinates()

    def __get_angle_cos(self):
        b = self.__l * math.cos((90 - self.__alpha) * math.pi / 180)   # xy plain
        lx = b * math.cos(self.__gamma * math.pi / 180)   # barrel x part
        ly = self.__l * math.cos(self.__alpha * math.pi / 180)   # barrel y part
        lz = b * math.sin(self.__gamma * math.pi / 180)   # barrel z part
        cosx = lx / self.__l
        cosy = ly / self.__l
        cosz = lz / self.__l
        directional_cos_array = np.array([cosx, cosy, cosz])
        return directional_cos_array

    def __get_barrel_coordinates(self):
        xe = self.__l * math.cos((90 - self.__alpha) * math.pi / 180) * math.cos(self.__gamma * math.pi / 180)   # barrel's end coordinate
        ze = self.__l * math.cos((90 - self.__alpha) * math.pi / 180) * math.sin(self.__gamma * math.pi / 180)   # barrel's end coordinate
        barrel_coordinates_array = np.array([xe, ze])
        return barrel_coordinates_array

    def __get_vector_advanced(self, time, mass, drag_coff, wind):
        cosx = self.__dir_cos[0]
        cosy = self.__dir_cos[1]
        cosz = self.__dir_cos[2]
        alpha = self.__alpha

        xe = self.__barrel_coordinates[0]
        ze = self.__barrel_coordinates[1]

        vm = self.__vm
        yb = self.__yb
        l = self.__l

        m = mass
        cd = drag_coff

        vw = wind.velocity
        gammaw = wind.gamma
        cw = wind.coefficient_wind

        sx1 = xe
        vx1 = vm * cosx
        sy1 = yb + l * math.cos(math.radians(alpha))




        vx1 = self.__vm *
    def __get_vector_simple(self, time):
        si = self.__vm * self.__dir_cos[0] * time + self.__barrel_coordinates[0]
        sj = (self.__yb + self.__l * math.cos(self.__alpha * math.pi / 180))\
            + (self.__vm * self.__dir_cos[1] * time)\
            - (0.5 * 9.81 * math.pow(time, 2))
        sk = self.__vm * self.__dir_cos[2] * time + self.__barrel_coordinates[1]
        vector = np.array([si, sj, sk])
        return vector

    def shoot(self, target, loop_interval, wind: Wind):
        time = float(0)
        vector = np.empty([3, 0])
        if isinstance(target, Target):
            while True:
                if self.__sim == "simple":
                    shell = self.__get_vector_simple(time)
                else:
                    shell = self.__get_vector_advanced(time, self.__mass, self.__drag_coff, wind)
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
                    time += loop_interval
                    continue
            return vector
        else:
            print("Target is not instance of Target class!!!")
            raise Exception
