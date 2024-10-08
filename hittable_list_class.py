from dataclasses import dataclass, field
from hittable_class import Hittable
from typing import List
from ray import ray
from HitRecord_class import HitRecord
from vec3_class import Vec3


@dataclass
class HittableList(Hittable):
    objects: List[Hittable] = field(default_factory=list)

    def add(self, obj: Hittable):
        self.objects.append(obj)

    def clear(self):
        self.objects.clear()

    def hit(self, ray: ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> bool:
        temp_rec = HitRecord(Vec3(), Vec3())  # Initialize with appropriate default values
        hit_anything = False
        closest_so_far = ray_tmax

        for obj in self.objects:
            if obj.hit(ray, ray_tmin, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.normal = temp_rec.normal
                rec.p = temp_rec.p
                rec.front_face = temp_rec.front_face
                rec.p = temp_rec.p

        return hit_anything
