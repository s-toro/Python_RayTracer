import typing
from vec3_class import Vec3

color = Vec3

def write_color(pixel_color: Vec3) -> None:
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    rbyte = int(255.999 * r)
    gbyte = int(255.999 * g)
    bbyte = int(255.999 * b)

    return f'{rbyte} {gbyte} {bbyte}\n'