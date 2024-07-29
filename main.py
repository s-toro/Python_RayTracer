def write_ppm_image(image_height, image_width):
    with open("ppm_image.ppm", 'w') as f:
        f.write(f'P3\n{image_width} {image_height}\n255\n')
        for i in range(0, image_width):
            for j in range(0, image_height):
                print(f'Scan lines remaining: {image_height - j}')
                r = float(i) / (image_width - 1)
                g = float(j) / (image_height - 1)
                b = 0.0
                ir = int(255.999 * r)
                ig = int(255.999 * g)
                ib = int(255.999 * b)
                f.write(f'{ir} {ig} {ib} ')
            print('\n')
    f.close()
    print('Finished writing ppm file.')

if __name__ == "__main__":
    write_ppm_image(256, 256)
