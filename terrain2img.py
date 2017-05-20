from PIL import Image
from convert_dict import CONVERT_DICT_SPRITES as CONVERT_DICT
from convert_dict import CONVERT_DICT_BINARY_REVERSE as BINARY


if __name__ == '__main__':
    import sys, glob
    if len(sys.argv) != 4:
        print('3 argument expected (text file, output filename, mode (t/b), {} provided'.format(len(sys.argv) - 1))
    elif len(glob.glob(sys.argv[1])) == 0:
        print('file doesn`t exist')
    else:
        terr = open(sys.argv[1])
        columns = []
        read = True
        while read:
            row = terr.readline()
            if len(row) == 0:
                read = False
            else:
                columns.append(row.split(' '))
        img = Image.new("RGB", (50 * (len(columns[0]) - 1), 50 * len(columns)))
        for y0 in range(len(columns)):
            for x0 in range(len(columns[0]) - 1):
                terr_type = columns[y0][x0] if sys.argv[3] == "t" else BINARY[columns[y0][x0]]
                shard = Image.open(CONVERT_DICT[terr_type])
                img.paste(shard, (x0 * 50, y0 * 50))
                shard.close()
        img.save(sys.argv[2], "PNG")