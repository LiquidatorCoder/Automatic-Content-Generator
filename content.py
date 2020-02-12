#-----------------------------
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from random import randint
import sys, os
from instapy_cli import client
#-----------------------------
from requests import get
from json import loads
#-----------------------------
# import requests
# from bs4 import BeautifulSoup
#-----------------------------
# pno = randint(1,10)
# result = requests.get(f'http://quotes.toscrape.com/page/{pno}/')
# page = result.text
# soup = BeautifulSoup(page, 'html.parser')
# quotes = soup.find_all('div', class_='quote')
# scraped = []
# for quote in quotes:
#     text = quote.find('span', class_='text').text
#     author = quote.find('small', class_='author').text
#     scraped.append([text, author])
#-----------------------------
# quotel = []
# auth = ""
# while len(quotel)>25 or len(quotel)==0:
#     qno = randint(0,9)
#     quotel = scraped[qno][0]
#     quotel = quotel.split(" ")
#     auth = f"- {scraped[qno][1]}"
# quote = ""
# c=0
# for i in quotel:
#     c+=1
#     if c>3:
#         quote = quote + "\n" + i + " "
#         c = 0
#     else:
#         quote = quote + i + " "
# quote = quote.replace('“','" ')
# quote = quote.replace('”',' "')
# text = quote + "\n\n" + auth
#-----------------------------
response = get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
while len(loads(response.text))>10 or len(loads(response.text))==0:
    response = get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
text1 = '{quoteText} - {quoteAuthor}'.format(**loads(response.text))
text1=text1.split(" ")
c=0
text = ""
for i in text1:
    c+=1
    if c>3:
        text = text + "\n" + i + " "
        c = 0
    else:
        text = text + i + " "
text = text.replace("  ","\n")
#-----------------------------
x=randint(1,9)
W, H = (1080,1080)
bg_path = os.path.join(os.getcwd(),"BG",f"{x}.png")
post = Image.open(bg_path)
draw = ImageDraw.Draw(post)
#-----------------------------
font = ImageFont.truetype(os.path.join(os.getcwd(),"Font","Montserrat-Medium.ttf"), 30)
draw.text((810, 1020),"@liquiatorcoder",(50,50,50),font=font)
#-----------------------------
font = ImageFont.truetype(os.path.join(os.getcwd(),"Font","Montserrat-SemiBoldItalic.ttf"), 70)
w, h = draw.textsize(text, font=font)
draw.text(((W-w)/2,(H-h)/2), text, (30,30,30), font = font)
#-----------------------------
post.save(os.path.join(os.getcwd(),"Post","post.png"))
#-----------------------------
username = 'motivation.py'
password = '30june2000'

image = os.path.join(os.getcwd(),"Post","post.png")
cap = '#motivation #motivationbot #getstarted #justdoit'
with client(username, password) as cli:
    cli.upload(image, cap)