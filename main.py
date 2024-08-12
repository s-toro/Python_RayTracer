import math

from color import color, write_color
from ray import ray
from vec3_class import Vec3
from hittable_list_class import HittableList
from hittable_class import Hittable
from HitRecord_class import HitRecord
from sphere import Sphere
from utility_functions_and_consts import *


def ray_color(r: ray, world: Hittable) -> Vec3:
    rec = HitRecord(p=Vec3(0, 0, 0), normal=Vec3(0, 0, 0))
    if world.hit(r, 0.01 , infinity, rec):
        return 0.5 * (rec.normal + color(1, 1, 1))
    unit_direction = Vec3.unit_vector(r.direction())
    a = 0.5*(unit_direction.y() + 1.0)
    print('2')
    return (1.0-a)*color(1.0, 1.0, 1.0) + a*color(0.5, 0.7, 1.0)


def write_ppm_image(image_width):
    aspect_ratio = 16.0 / 9.0

    image_height = int(image_width / aspect_ratio)
    if image_height < 1:
        image_height = 1

    world = HittableList()
    world.add(Sphere(Vec3(0, 0, -1), 0.5))
    world.add(Sphere(Vec3(0, -100.5, -1), 100))
    focal_length = 1.0
    viewport_height = 2.0
    viewport_width = viewport_height * (image_width/image_height)
    camera_center = Vec3(0, 0, 0)
    viewport_u = Vec3(viewport_width, 0, 0)
    viewport_v = Vec3(0, -viewport_height, 0)

    pixel_delta_u = viewport_u / image_width
    pixel_delta_v = viewport_v / image_height

    viewport_upper_left = camera_center - Vec3(0, 0, focal_length) - viewport_u/2 - viewport_v/2
    pixel100_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

    with open("ppm_image.ppm", 'w') as f:
        f.write(f'P3\n{image_width} {image_height}\n255\n')
        for i in range(image_height):
            print(f'Scan lines remaining: {image_height - i}')
            for j in range(image_width):
                pixel_center = pixel100_loc + (j*pixel_delta_u) + (i*pixel_delta_v)
                ray_direction = Vec3.unit_vector(pixel_center - camera_center)
                r = ray(camera_center, ray_direction)
                pixel_color = ray_color(r, world)
                f.write(str(write_color(pixel_color)))
                f.write('\n')
    print('Finished writing ppm file.')


if __name__ == "__main__":
    write_ppm_image(400)
