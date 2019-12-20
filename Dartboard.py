import math
import cmath
import random
import Shot

class Dartboard:
    def __init__(self):
        self.bullseye = 1

    def __calcDistance(self, shot):
        return math.sqrt(shot.getX()**2 + shot.getY()**2)

    def shoot(self):
        return random.uniform(-1, 1), random.uniform(-1, 1)

    def isIn(self, shot):
        if self.__calcDistance(shot) < self.bullseye:
            return True
        else:
            return False

    def shrinkBoard(self, shot):
        shotDistance = self.__calcDistance(shot)
        self.bullseye = math.sqrt(self.bullseye**2 - shotDistance**2)
        return self.bullseye
