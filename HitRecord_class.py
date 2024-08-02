from dataclasses import dataclass
from vec3_class import Vec3


@dataclass
class HitRecord:
    p: Vec3
    normal: Vec3
    t: float