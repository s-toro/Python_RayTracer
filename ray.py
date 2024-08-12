from vec3_class import Vec3

class ray():
    def __init__(self, origin: Vec3, direction: Vec3):
        self.dir = direction
        self.orig = origin

    def origin(self):
        return self.orig

    def direction(self):
        return self.dir

    def at(self, t):
        return self.orig + (t*self.dir)