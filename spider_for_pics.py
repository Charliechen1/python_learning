import requests
from bs4 import BeautifulSoup
import urllib.request
import random
import os

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url='http://bbs.h5galgame.me/forum.php?mod=forumdisplay&fid=142&page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        fw = open('source.txt','w')
        for link in soup.findAll('a',{'class': 's xst'}):
            href = link.get('href')
            title = link.string
            #print("title:" + title)
            #fw.write("title:" + title + "\n")
            get_single_item_data(href,fw)
            #print("--------------------------------------------------");
            #fw.write("--------------------------------------------------\n")
        page += 1
        fw.close()

def get_single_item_data(url,fw):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    if not os.path.exists('pics'):
        os.mkdir('pics')
    for img in soup.findAll('img'):
        img_src = img.get('src')
        if 'http' not in img_src:
            img_src = "http://bbs.h5galgame.me/" + img_src
        download_web_img(img_src)

def download_web_img(url):
    name = random.randrange(1,10000000)
    full_name = "pics/" + str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

trade_spider(1)
