from typing import List

from math import sqrt, pi, cos, sin
from random import random


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        length = sqrt(random()) * self.radius
        deg = random()*2*pi
        x = self.x_center + length * cos(deg)
        y = self.y_center + length * sin(deg)
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
