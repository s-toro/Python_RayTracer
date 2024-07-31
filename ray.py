from vec3_class import Vec3

class ray():
    def __init__(self, direction: Vec3, origin: Vec3):
        self.dir = direction
        self.orig = origin

    def origin(self):
        return self.orig

    def direction(self):
        return self.dir

    def at(self, t):
        return self.orig + (t*self.dir)