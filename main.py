from color import color, write_color
from ray import ray
from vec3_class import Vec3


def ray_color(r: ray) -> Vec3:
    unit_direction = Vec3.unit_vector(r.direction())
    a = 0.5*(unit_direction.y() + 1.0)
    return (1.0-a)*color(1.0, 1.0, 1.0) + a*color(0.5, 0.7, 1.0)

def write_ppm_image(image_height, image_width):
    aspect_ratio = 16.0 / 9.0
    image_width = 400

    image_height = int(image_width / aspect_ratio)
    if image_height < 1:
        image_height = 1

    focal_length  = 1.0
    viewport_height = 2.0
    viewport_width = viewport_height * (image_width/image_height)
    camera_center = Vec3(0, 0, 0)
    viewport_u = Vec3(viewport_width, 0, 0)
    viewport_v = Vec3(0, (-2.0), 0)

    pixel_delta_u = viewport_u / image_width
    pixel_delta_v = viewport_v / image_height

    viewport_upper_left = camera_center - Vec3(0, 0, focal_length) - viewport_u/2 - viewport_v/2
    pixel100_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

    with open("ppm_image.ppm", 'w') as f:
        f.write(f'P3\n{image_width} {image_height}\n255\n')
        for i in range(0, image_height):
            for j in range(0, image_width):
                pixel_center = pixel100_loc + (i*pixel_delta_u) + (j*pixel_delta_v)
                ray_direction = pixel_center - camera_center
                r = ray(camera_center, ray_direction)
                pixel_color = ray_color(r)
                print(f'Scan lines remaining: {image_height - j}')
                f.write(str(write_color(pixel_color)))
                f.write('\n')
    f.close()
    print('Finished writing ppm file.')

if __name__ == "__main__":
    write_ppm_image(256, 256)
