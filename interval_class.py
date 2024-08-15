from dataclasses import dataclass
from utility_functions_and_consts import *

@dataclass
class Interval():
    min : float(infinity) = -infinity
    max : float(infinity) = +infinity

    def size(self):
        return max - min

    def containst(self, x: float) -> bool:
        return self.min <= x & x <= self.max

    def surrouds(self, x: float):
        return self.min < x & x < self.max
