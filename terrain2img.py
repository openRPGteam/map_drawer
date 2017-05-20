from PIL import Image

CONVERT_DICT = {
    "WATER" : "sprites/water.png",
    "GRASS": "sprites/grass.png",
    "SAND" : "sprites/sand.png",
    "MOUNTAIN" : "sprites/mountain.png",
    "SNOW" : 'sprites/snow.png'
}

if __name__ == '__main__':
    import sys, glob
    if len(sys.argv) != 3:
        print('2 argument expected, {} provided'.format(len(sys.argv) - 1))
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
        img = Image.new("RGB", (50 * len(columns), 50 * len(columns[0])))
        for y0 in range(len(columns)):
            for x0 in range(len(columns[0]) - 1):
                shard = Image.open(CONVERT_DICT[columns[x0][y0]])
                img.paste(shard, (x0 * 50, y0 * 50))
                shard.close()
        img.save(sys.argv[2], "PNG")