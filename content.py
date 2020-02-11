from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from random import randint
import sys, os

x=randint(1,9)
# path = os.path.abspath('.')
bg_path = f"C:\\Users\\Asus\\Desktop\\AutomaticContentCreator\\BG\\{x}.png"
post = Image.open(bg_path)
draw = ImageDraw.Draw(post)
font = ImageFont.truetype("C:\\Users\\Asus\\Desktop\\AutomaticContentCreator\\Font\\Montserrat-Medium.ttf", 160)
draw.text((0, 0),"Sample Text",(50,50,50),font=font)
post.save(f"C:\\Users\\Asus\\Desktop\\AutomaticContentCreator\\post.png")

post.show()