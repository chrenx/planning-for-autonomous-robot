import math


class City:
    def __init__(self, r, theta):
        self._r = r
        self._theta = theta

    def get_distance(self, city):
        theta1 = math.radians(self._theta)
        theta2 = math.radians(city.get_theta())
        distance = math.sqrt(self._r ** 2 + city.get_r() ** 2 - 2 * self._r * city.get_r() * math.cos(theta1 - theta2))
        return distance

    def get_r(self):
        return self._r

    def get_theta(self):
        return self._theta

    def __repr__(self):
        return "(" + str(self._r) + "," + str(self._theta) + ")"
