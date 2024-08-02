import math


class Vec3:
    def __init__(self, e0=0, e1=0, e2=0):
        self.e = [e0, e1, e2]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])

    def __getitem__(self, i):
        return self.e[i]

    def __setitem__(self, i, value):
        self.e[i] = value

    def __iadd__(self, v):
        if isinstance(v, Vec3):
            self.e[0] += v.e[0]
            self.e[1] += v.e[1]
            self.e[2] += v.e[2]
            return self
        else:
            raise TypeError('Operands must be of type Vec3')

    def __imul__(self, t):
        if isinstance(t, (int, float)):
            self.e[0] *= t
            self.e[1] *= t
            self.e[2] *= t

    def __itruediv__(self, t):
        if not isinstance(t, (float, int)):
            raise TypeError("Must multiply by a int of float")
        if t == 0:
            raise ZeroDivisionError("Division by zero")
        return self.__imul__(1 / t)

    def __truediv__(self, t):
        return self.__mul__(1/t)

    def length(self):
        length_sqrd = self.length_sqrd()
        return math.sqrt(length_sqrd)

    def length_sqrd(self):
        return self.e[0] * self.e[0] + self.e[1] * self.e[1] + self.e[2] * self.e[2]

    def __str__(self):
        return f'{self.e[0]} {self.e[1]} {self.e[2]}'

    def __repr__(self):
        return f'Vec3({self.e[0]} {self.e[1]} {self.e[2]})'

    def __add__(self, v):
        if isinstance(v, Vec3):
            return Vec3(self.e[0] + v.e[0], self.e[1] + v.e[1], self.e[2] + v.e[2])
        else:
            raise TypeError("Vec3 object needs to be added up with another Vec3 object.")

    def __sub__(self, v):
        if isinstance(v, Vec3):
            return Vec3(self.e[0] - v.e[0], self.e[1] - v.e[1], self.e[2] - v.e[2])
        else:
            raise TypeError("Vec3 object needs to be substracted with another Vec3 object.")

    def __mul__(self, t):
        if isinstance(t, (int, float)):
            return Vec3(t * self.e[0], t * self.e[1], t * self.e[2])
        elif isinstance(t, Vec3):
            return Vec3(t.e[0] * self.e[0], t.e[1] * self.e[1], t.e[2] * self.e[2])
        else:
            raise TypeError("You can multiply a Vec3 object with either another Vec3 object or with int/float")

    def __rmul__(self, other):
        return self.__mul__(other)

    @staticmethod
    def dot(v, u):
      return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

    @staticmethod
    def cross(v, u):
        return Vec3(u.e[1] * v.e[2] - u.e[2] * v.e[1],
                    u.e[2]*v.e[0] - u.e[0] * v.e[2],
                    u.e[0] * v.e[1] - u.e[1] * v.e[0])

    @staticmethod
    def unit_vector(v):
        if isinstance(v, Vec3):
            return v / v.length()
        else:
            raise TypeError("Static method unit_vector accepts only instances of Vec3")


point3 = Vec3

# Example usage
if __name__ == "__main__":
    v1 = Vec3()  # Default constructor, v1 = (0, 0, 0)
    v2 = Vec3(1, 2, 3)  # Parameterized constructor, v2 = (1, 2, 3)

    x = v2.x()  # Access x component, x = 1
    y = v2.y()  # Access y component, y = 2
    z = v2.z()  # Access z component, z = 3

    v3 = -v2  # Negate v2, v3 = (-1, -2, -3)

    value = v2[1]  # Access component using subscript, value = 2
    v2[1] = 10  # Modify y component, v2 = (1, 10, 3)

    print(f"v1: ({v1.x()}, {v1.y()}, {v1.z()})")
    print(f"v2: ({v2.x()}, {v2.y()}, {v2.z()})")
    print(f"v3: ({v3.x()}, {v3.y()}, {v3.z()})")
    v3 = v3 * 2
    print(f"{v3}")
    v3 = -1 * v3
    print(f"{v3}")
    print(f"v2 * v3 = {v2 * v3}")
    print(f"{v3/2}")
    print(f"value: {value}")
    print(f"{Vec3.dot(v2, v3)}")
    v4 = Vec3(float(-value), 0.0, 0.0)
    print(f'{v4}')
