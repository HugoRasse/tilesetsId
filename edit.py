import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import numpy as np

def write(pPath, pCols, pLines, pTileW, pTileH):
    try:
        image = PIL.Image.open(pPath)
        width,height = image.size
        draw = PIL.ImageDraw.Draw(image)
        font = PIL.ImageFont.truetype("font.ttf", 50)

        id = 1
        for l in range(pLines):
            for c in range(pCols):
                draw.text((c * pTileW, l * pTileH), str(id), (255,255,255), font=font)
                id += 1


        image.save("tiles.png")
    except Exception as e:
        print(e)

write("tiles.png", 8, 8, 256, 256)