from abc import ABC, abstractmethod
from HitRecord_class import HitRecord

class Hittable(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def hit(self, r, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> bool:
        ...