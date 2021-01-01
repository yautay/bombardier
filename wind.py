class Wind:
    def __init__(self, velocity, gamma, cw = 10):
        self.__v = velocity
        self.__gammaV = gamma
        self.__cw = cw

    @property
    def velocity(self):
        return self.__v

    @property
    def gamma(self):
        return self.__gammaV

    @property
    def coefficient_wind(self):
        return self.__cw
