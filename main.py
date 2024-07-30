from color import color, write_color
def write_ppm_image(image_height, image_width):
    with open("ppm_image.ppm", 'w') as f:
        f.write(f'P3\n{image_width} {image_height}\n255\n')
        for i in range(0, image_width):
            for j in range(0, image_height):
                print(f'Scan lines remaining: {image_height - j}')
                pixel_color = color(i/(image_width-1), j/(image_height-1), 0)
                f.write(str(write_color(pixel_color)))
                f.write('\n')
    f.close()
    print('Finished writing ppm file.')

if __name__ == "__main__":
    write_ppm_image(256, 256)
