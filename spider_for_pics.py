import requests
from bs4 import BeautifulSoup
import urllib.request
import random
import os

website='http://desk.zol.com.cn/'

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url='http://desk.zol.com.cn/2560x1600/' + str(page)+'.html'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        fw = open('source.txt','w')
        for link in soup.findAll('a',{'class': 'pic'}):
            href = link.get('href')
            if 'http' not in href:
                href = website + href
            get_single_item_data(href,fw)
        page += 1
        fw.close()

def get_single_item_data(url,fw):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    if not os.path.exists('pics'):
        os.mkdir('pics')
    for img in soup.findAll('img',{'id' : 'bigImg'}):
        img_src = img.get('src')
        download_web_img(img_src)

def download_web_img(url):
    name = random.randrange(1,10000000)
    full_name = "pics/" + str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

trade_spider(1)
