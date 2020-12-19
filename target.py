import numpy as np


class Target:
    def __init__(self, x, y, z, l, w, h):
        self.x = x
        self.y = y
        self.z = z
        self.l = l
        self.w = w
        self.h = h
        self.coordinates = self.__get_target_coordinates()

    def __get_target_coordinates(self):
        x = self.x
        y = self.y
        z = self.z
        l = self.l
        w = self.w
        h = self.h
        tx1 = x - l / 2
        tx2 = x + l / 2
        ty1 = y - h / 2
        ty2 = y + h / 2
        tz1 = z - w / 2
        tz2 = z + w / 2
        target_coordinates = np.array([tx1, tx2, ty1, ty2, tz1, tz2])
        return target_coordinates

    def check_hit(self, muzzle_vector):
        cr = self.coordinates
        if cr[1] >= muzzle_vector[0] >= cr[0]:
            if cr[3] <= muzzle_vector[1] >= cr[2]:
                if cr[5] <= muzzle_vector[2] >= cr[4]:
                    return 1   # target hit
        if muzzle_vector[1] < 0:
            return 2   # plane hit
        return 0   # no impact
