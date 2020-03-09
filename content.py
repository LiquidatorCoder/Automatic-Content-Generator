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
import numpy as np
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
def alpha_composite(src, dst):
    '''
    Return the alpha composite of src and dst.

    Parameters:
    src -- PIL RGBA Image object
    dst -- PIL RGBA Image object

    The algorithm comes from http://en.wikipedia.org/wiki/Alpha_compositing
    '''
    # http://stackoverflow.com/a/3375291/190597
    # http://stackoverflow.com/a/9166671/190597
    src = np.asarray(src)
    dst = np.asarray(dst)
    out = np.empty(src.shape, dtype = 'float')
    alpha = np.index_exp[:, :, 3:]
    rgb = np.index_exp[:, :, :3]
    src_a = src[alpha]/255.0
    dst_a = dst[alpha]/255.0
    out[alpha] = src_a+dst_a*(1-src_a)
    old_setting = np.seterr(invalid = 'ignore')
    out[rgb] = (src[rgb]*src_a + dst[rgb]*dst_a*(1-src_a))/out[alpha]
    np.seterr(**old_setting)
    out[alpha] *= 255
    np.clip(out,0,255)
    # astype('uint8') maps np.nan (and np.inf) to 0
    out = out.astype('uint8')
    out = Image.fromarray(out, 'RGBA')
    return out
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
x1 = randint(1, 9)
W, H = (1080, 1080)
bg_path1 = os.path.join(os.getcwd(), "BG", f"{x1}.png")
x2 = randint(1, 9)
W, H = (1080, 1080)
bg_path2 = os.path.join(os.getcwd(), "BG", f"{x2}.png")
im1 = Image.open(bg_path1)
im2 = Image.open(bg_path2)
post = alpha_composite(im1, im2)

draw = ImageDraw.Draw(post)
# -----------------------------
fontlist = ["Montserrat-Black.ttf","Montserrat-BlackItalic.ttf","Montserrat-Bold.ttf","Montserrat-BoldItalic.ttf","Montserrat-ExtraBold.ttf","Montserrat-ExtraBoldItalic.ttf","Montserrat-ExtraLight.ttf","Montserrat-ExtraLightItalic.ttf","Montserrat-Italic.ttf","Montserrat-Light.ttf","Montserrat-LightItalic.ttf","Montserrat-Medium.ttf","Montserrat-MediumItalic.ttf","Montserrat-Regular.ttf","Montserrat-SemiBold.ttf","Montserrat-SemiBoldItalic.ttf","Montserrat-Thin.ttf","Montserrat-ThinItalic.ttf"]
fontnumber = randint(0,17)
fontname = fontlist[fontnumber]
font = ImageFont.truetype(
    os.path.join(
        os.getcwd(),
        "Font",
        fontname),
    30)
str = input("Enter the signing name with @ : ")
draw.text((760, 1000), str, (50, 50, 50), font=font)
# -----------------------------
fontnumber2 = randint(0,17)
fontname2 = fontlist[fontnumber2]
font = ImageFont.truetype(
    os.path.join(
        os.getcwd(),
        "Font",
        fontname2),
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

browser = webdriver.Chrome(r"C:\Users\aksha\OneDrive\Desktop\Automatic Content\Automatic-Content-Generator\chromedriver.exe",options=options)
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
caption = caption + "\n.\n.\n.\n.\n.\n.\n.\n.\n#motivation #getstarted #nevergiveup #dontgiveup #happy #life #goals"
browser.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section[1]/div[1]/textarea").send_keys(caption)
n = randint(2,5)
time.sleep(n)
browser.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button").click()
n = randint(5,7)
time.sleep(n)
#browser.close()