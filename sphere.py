from math import sqrt
from hittable_class import Hittable
from ray import ray
from vec3_class import Vec3
from HitRecord_class import HitRecord


class Sphere(Hittable):
    def __init__(self, center: Vec3, radius: float):
        self.center = center
        self.radius = max(0, radius)

    def hit(self, r: ray, ray_tmin: float, ray_tmax: float,rec: HitRecord) -> bool:
        oc =  self.center - r.origin()
        a = r.direction().length_sqrd()
        h = Vec3.dot(r.direction(), oc)
        c = oc.length_sqrd() - self.radius*self.radius

        discriminant = h*h - a*c
        if discriminant < 0:
            return False

        sqrtd = sqrt(discriminant)
        root = (h - sqrtd) / a
        if root < ray_tmin or root > ray_tmax:
            root = (h + sqrtd) / a
            if root < ray_tmin or ray_tmax < root:
                return False

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)
        return True

