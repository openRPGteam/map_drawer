from PIL import Image, ImageFilter
from convert_dict import CONVERT_DICT_TEXTMAP as CONVERT_DICT
from convert_dict import CONVERT_DICT_BINARY as BINARY


def get_distance(color1, color2):
    return sum([abs(color1[x] - color2[x]) for x in range(len(color1))])


def closest_match(color, mode="t"):
    distances = [get_distance(color, cl) for cl in CONVERT_DICT.keys()]
    text_val = CONVERT_DICT[tuple(CONVERT_DICT.keys())[distances.index(min(distances))]]
    if mode == "t":
        return text_val
    elif mode == "b":
        return str(BINARY[text_val])
    else:
        return None


def evaluate_color(image, x, y, sizen, mode="t"):
    cropbox = (x * sizen, y * sizen, (x + 1) * sizen, (y + 1) * sizen)
    shard = image.crop(cropbox).filter(ImageFilter.GaussianBlur(sizen ** 3))
    return closest_match(shard.getpixel((sizen//2, sizen//2)), mode)


def process(image, size, mode="t"):
    type_list = []
    for y in range(image.size[1] // size):
        row = []
        for x in range(image.size[0] // size):
            row.append(evaluate_color(image, x, y, size, mode))
        type_list.append(row)
    return type_list

if __name__ == '__main__':
    import glob, sys
    if len(sys.argv) != 4:
        print('3 arguments excepted (filename, cell size, mode (t/b)), {} provided'.format(len(sys.argv) - 1))
    elif len(glob.glob(sys.argv[1])) == 0:
        print('file doesn`t exist')
    else:
        img = Image.open(sys.argv[1])
        size = int(sys.argv[2])
        if img.size[0] >= size and img.size[1] >= size:
            result = process(img, size, sys.argv[3])
            for row in result:
                rowstr = ""
                for elem in row:
                    rowstr += elem + ' '
                print(rowstr)
            img.close()
        else:
            print('cell size must be smaller than image size!')

