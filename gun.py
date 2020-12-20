import math
import numpy as np


class Gun:
    def __init__(self, vm, alpha, gamma, l, yb):
        self.vm = vm   # muzzle velocity m/s
        self.alpha = alpha   # vertical inclination
        self.gamma = gamma   # horizontal azimuth
        self.l = l   # barrel length
        self.yb = yb   # gun elevation
        self.dir_cos = self.__get_angle_cos()
        self.barrel_coordinates = self.__get_barrel_coordinates()

    def __get_angle_cos(self):
        b = self.l * math.cos((90 - self.alpha) * math.pi / 180)   # xy plain
        lx = b * math.cos(self.gamma * math.pi / 180)   # barrel x part
        ly = self.l * math.cos(self.alpha * math.pi / 180)   # barrel y part
        lz = b * math.sin(self.gamma * math.pi / 180)   # barrel z part
        cosx = lx / self.l
        cosy = ly / self.l
        cosz = lz / self.l
        directional_cos_array = np.array([cosx, cosy, cosz])
        return directional_cos_array

    def __get_barrel_coordinates(self):
        xe = self.l * math.cos((90 - self.alpha) * math.pi / 180) * math.cos(self.gamma * math.pi / 180)   # barrel's end coordinate
        ze = self.l * math.cos((90 - self.alpha) * math.pi / 180) * math.sin(self.gamma * math.pi / 180)   # barrel's end coordinate
        barrel_coordinates_array = np.array([xe, ze])
        return barrel_coordinates_array

    def get_shell_vector(self, time):
        si = self.vm * self.dir_cos[0] * time + self.barrel_coordinates[0]
        sj = (self.yb + self.l * math.cos(self.alpha * math.pi / 180))\
            + (self.vm * self.dir_cos[1] * time)\
            - (0.5 * 9.81 * math.pow(time, 2))
        sk = self.vm * self.dir_cos[2] * time + self.barrel_coordinates[1]
        vector = np.array([si, sj, sk])
        return vector
