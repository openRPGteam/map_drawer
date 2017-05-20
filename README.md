# map_drawer
## generate text map from image
```
pip3 install -r requirements.txt
python3 img2terrain.py [image] [cell size in pixels] [mode(t=text/b=binary)]
```
Example:
```
python3 img2terrain.py ~/map.png 50 b
```
## generate image from text map
```
pip3 install -r requirements.txt
python3 terrain2img.py [text file containing text map] [output image filename (.png)] [mode(t=text/b=binary)]
```
Example:
```
python3 terrain2img.py ~/image_map.txt ~/image_from_map.png t
```
