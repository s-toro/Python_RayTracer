from dataclasses import dataclass
from vec3_class import Vec3
from ray import ray


@dataclass
class HitRecord:
    p: Vec3
    normal: Vec3
    t: float
    front_face: bool

    def set_face_normal(self, r: ray, outward_normal: Vec3):
        self.front_face = bool(Vec3.dot(r.direction(), outward_normal) < 0 )
        self.normal = outward_normal
        if not self.front_face:
            self.normal *= -1