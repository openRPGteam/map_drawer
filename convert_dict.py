CONVERT_DICT_SPRITES = {
    "WATER" : "sprites/water.png",
    "GRASS": "sprites/grass.png",
    "SAND" : "sprites/sand.png",
    "MOUNTAIN" : "sprites/mountain.png",
    "SNOW" : 'sprites/snow.png',
    "MUD" : "sprites/mud.png",
    "WHEAT" : "sprites/wheat.png",
    "FOREST" : "sprites/dark_grass.png",
    "ASHES" : "sprites/ash.png"
}

CONVERT_DICT_TEXTMAP = {
    (86, 102, 99) : "WATER",
    (152, 171, 79) : "GRASS",
    (122, 83, 50) : "MUD",
    (161, 145, 109) : "SAND",
    (82, 81, 60) : "MOUNTAIN",
    (193, 201, 204) : "SNOW",
    (214, 198, 136) : "WHEAT",
    (68, 72, 45) : "FOREST",
    (82, 81, 76) : "ASHES"
}

CONVERT_DICT_BINARY = {
    "GRASS" : 0,
    "WATER" : 1,
    "MUD" : 2,
    "SAND": 3,
    "MOUNTAIN" : 4,
    "SNOW" : 5,
    "WHEAT" : 6,
    "FOREST": 7,
    "ASHES" : 8
}

CONVERT_DICT_BINARY_REVERSE = {}
for terrain_type in CONVERT_DICT_BINARY.keys():
    CONVERT_DICT_BINARY_REVERSE[str(CONVERT_DICT_BINARY[terrain_type])] = terrain_type