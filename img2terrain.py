from PIL import Image, ImageFilter

CONVERT_DICT = {
    (59, 100, 79) : "WATER",
    (82, 121, 63) : "GRASS",
    (161, 145, 109) : "SAND",
    (134, 123, 95) : "MOUNTAIN",
    (167, 163, 154) : "SNOW"
}


def get_distance(color1, color2):
    return sum([abs(color1[x] - color2[x]) for x in range(len(color1))])


def closest_match(color):
    distances = [get_distance(color, cl) for cl in CONVERT_DICT.keys()]
    return CONVERT_DICT[tuple(CONVERT_DICT.keys())[distances.index(min(distances))]]


def evaluate_color(image, x, y, sizen):
    cropbox = (x * sizen, y * sizen, (x + 1) * sizen, (y + 1) * sizen)
    shard = image.crop(cropbox).filter(ImageFilter.GaussianBlur(sizen ** 3))
    return closest_match(shard.getpixel((sizen//2, sizen//2)))


def process(image, size):
    type_list = []
    for y in range(image.size[1] // size):
        row = []
        for x in range(image.size[0] // size):
            row.append(evaluate_color(image, x, y, size))
        type_list.append(row)
    return type_list

if __name__ == '__main__':
    import glob, sys
    if len(sys.argv) != 3:
        print('2 arguments excepted (filename, cell size), {} provided'.format(len(sys.argv) - 1))
    elif len(glob.glob(sys.argv[1])) == 0:
        print('file doesn`t exist')
    else:
        img = Image.open(sys.argv[1])
        size = int(sys.argv[2])
        if img.size[0] >= size and img.size[1] >= size:
            result = process(img, size)
            for row in result:
                rowstr = ""
                for elem in row:
                    rowstr += elem + ' '
                print(rowstr)
            img.close()
        else:
            print('cell size must be smaller than image size!')

