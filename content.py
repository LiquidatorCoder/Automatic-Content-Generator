from PIL import Image,ImageDraw
from random import randint as rint
 
def random_gradient(name):
    img = Image.new("RGBA", (1080,1080), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    #r,g,b = rint(0,255), rint(0,255), rint(0,255)
    r,g,b = 253, 110, 106
    #dr = (rint(0,255) - r)/500.
    #dg = (rint(0,255) - g)/500.
    #db = (rint(0,255) - b)/500.
    dr,dg,db = 255/2000, 198/2000, 0/2000
    for i in range(1580):
        r,g,b = r+dr, g+dg, b+db
        draw.line((0,i,1080,i-500), fill=(int(r),int(g),int(b)))

    img.save(name+".png", "PNG")
# img = Image.new('RGBA', (1080, 1080), color = (253, 110, 106))
# img.save('test.png')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-





if __name__ == "__main__":
    for name in range(1):
        random_gradient(str(name))