# -----------------------------
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from random import randint
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import *
import autoit
# -----------------------------
from requests import get
from json import loads
# -----------------------------
# import requests
# from bs4 import BeautifulSoup
# -----------------------------
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
# -----------------------------
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
# -----------------------------
response = get(
    'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
while len(loads(response.text)) > 10 or len(loads(response.text)) == 0:
    response = get(
        'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
text1 = '{quoteText} - {quoteAuthor}'.format(**loads(response.text))
text1 = text1.split(" ")
c = 0
text = ""
for i in text1:
    c += 1
    if c > 3:
        text = text + "\n" + i + " "
        c = 0
    else:
        text = text + i + " "
text = text.replace("  ", "\n")
# -----------------------------
x = randint(1, 9)
W, H = (1080, 1080)
bg_path = os.path.join(os.getcwd(), "BG", f"{x}.png")
post = Image.open(bg_path)
draw = ImageDraw.Draw(post)
# -----------------------------
font = ImageFont.truetype(
    os.path.join(
        os.getcwd(),
        "Font",
        "Montserrat-Medium.ttf"),
    30)
draw.text((810, 1020), "@motivation.py", (50, 50, 50), font=font)
# -----------------------------
font = ImageFont.truetype(
    os.path.join(
        os.getcwd(),
        "Font",
        "Montserrat-SemiBoldItalic.ttf"),
    70)
w, h = draw.textsize(text, font=font)
draw.text(((W - w) / 2, (H - h) / 2), text, (30, 30, 30), font=font)
# -----------------------------
post.save(os.path.join(os.getcwd(), "Post", "post.png"))
# -----------------------------

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
#mobile_emulation = {"deviceName": "Nexus 5"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')

# -----------------------------

browser = webdriver.Chrome(options=options)
username = 'motivation.py'
password = '30june2000'
browser.get('https://www.instagram.com/accounts/login/')

n = randint(3,5)
time.sleep(n)
usernameInput = browser.find_elements_by_css_selector('form input')[0]
passwordInput = browser.find_elements_by_css_selector('form input')[1]

usernameInput.send_keys(username)
passwordInput.send_keys(password)
passwordInput.send_keys(Keys.ENTER)
n = randint(3,5)
time.sleep(n)
browser.find_element_by_xpath("/html/body/div[1]/section/main/div/button").click()
n = randint(2,5)
time.sleep(n)
browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
# while 1:
#     time.sleep(1)
#     try:
#         driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
#         break
#     except:
#         pass
n = randint(2,5)
time.sleep(n)
browser.find_element_by_xpath("/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]").click()
autoit.win_active("Open") #open can change by your os language if not open change that
n = randint(2,5)
time.sleep(n)
autoit.control_send("Open", "Edit1", os.path.join(os.getcwd(), "Post", "post.png"))
n = randint(2,5)
time.sleep(n)
autoit.control_send("Open", "Edit1", "{ENTER}")
n = randint(2,5)
time.sleep(n)
browser.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button").click()
n = randint(2,5)
time.sleep(n)
caption = text.replace("\n", " ")
browser.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section[1]/div[1]/textarea").send_keys(caption)
n = randint(2,5)
time.sleep(n)
browser.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button").click()
n = randint(5,7)
time.sleep(n)
#browser.close()