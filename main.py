import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from pathlib import Path
import csv

from mintlemon import Normalizer

###########################   Data Selection   #######################################

'''

driver = webdriver.Chrome()
driver.get("https://www.trthaber.com/tum-mansetler.html")
scroll_pause_time = 4
screen_height = driver.execute_script("return window.screen.height;")
i = 1

while (True):
    driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if screen_height * i > scroll_height:
        break

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

titleDiv = soup.find_all(class_='title')
news = [];
for title in titleDiv:
    text = title.find('a')['title']
    news.append(text)
    
'''

news = []

def getData(url,format,item,element):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,format)
    item = soup.find_all(item)
    for title in item:
        text = title.find(element).text
        news.append(text)

# getData("https://www.milliyet.com.tr/rss/rssnew/teknolojirss.xml","xml","item","title")
# getData("https://www.haberturk.com/rss/kategori/teknoloji.xml","xml","item","title")
# getData("https://www.sozcu.com.tr/feeds-rss-category-bilim-teknoloji","xml","item","title")
# getData("https://www.manisamansetgazetesi.com/rss/teknoloji-50","xml","item","title")
# getData("https://www.aspor.com.tr/rss/sampiyonlar-ligi.xml","xml","item","title")
# getData("https://www.ahaber.com.tr/rss/saglik.xml","xml","item","title")
# getData("https://www.saglikpersonelihaber.com/rss.xml","xml","item","title")
# getData("https://www.saglikbulvari.com/rss_saglik_12.xml","xml","item","title")
# getData("https://www.blokhaber.com/rss/ekonomi.xml","xml","item","title")
# getData("https://www.ekonomimedya.com.tr/rss_ekonomi_6.xml","xml","item","title")
# getData("https://www.newsfindy.com/rss/ekonomi.xml","xml","item","title")
# getData("https://www.saglikhaberajansi.com/rss_saglik-bakanligi_80.xml","xml","item","title")
# getData("https://t24.com.tr/rss/haber/bilim-teknoloji","xml","item","title")
# getData("https://www.manisamansetgazetesi.com/rss/spor-13","xml","item","title")
# getData("https://www.milliyet.com.tr/rss/rssnew/gundemrss.xml","xml","item","title")
# getData("https://www.milliyet.com.tr/rss/rssnew/siyasetrss.xml","xml","item","title")
# getData("https://www.personelsaglikhaber.com.tr/rss/saglik.xml","xml","item","title")
# getData("https://www.ntv.com.tr/saglik.rss","xml","entry","title")
# getData("https://www.haberturk.com/rss/ekonomi.xml","xml","item","title")
# getData("https://www.ntv.com.tr/ekonomi.rss","xml","entry","title")
# getData("https://www.ekonomidunya.com/rss_ekonomi_1.xml","xml","item","title")
# getData("https://www.krediveborsa.com/rss/ekonomi-5","xml","item","title")
# getData("https://www.ekonomiege.com/rss.xml","xml","item","title")
# getData("https://www.muhalif.com.tr/rss/saglik-6","xml","item","title")
# getData("https://www.ensonhaber.com/rss/saglik.xml","xml","item","title")
# getData("https://www.sozcu.com.tr/feeds-rss-category-saglik","xml","item","title")
# getData("https://www.futboo.com/rss.xml","xml","item","title")
# getData("https://www.spormaraton.com/rss/","xml","item","title")
# getData("https://www.mynet.com/haber/rss/kategori/teknoloji/","xml","item","title")
# getData("https://www.haberturk.com/rss/kategori/teknoloji.xml","xml","item","title")
# getData("https://haberglobal.com.tr/rss/bilim-teknoloji","xml","item","title")
# getData("https://www.inovatifhaber.com/rss/bilim-teknoloji.xml","xml","item","title")
# getData("https://www.inovatifhaber.com/rss/guncel.xml","xml","item","title")
# getData("https://t24.com.tr/rss/haber/gundem","xml","item","title")
# getData("https://www.inovatifhaber.com/rss/siyaset.xml","xml","item","title")
# getData("https://www.siyasetgercegi.com/rss_siyaset_22.xml","xml","item","title")
# getData("https://www.ekonomitime.com/rss/ekonomi-5","xml","item","title")
# getData("https://www.ekonomitime.com/rss/spor-4","xml","item","title")
# getData("https://www.gundemdeyiz.com/rss/gundem-8","xml","item","title")
# getData("https://www.trthaber.com/saglik_articles.rss","xml","item","title")
# getData("https://www.trthaber.com/bilim_teknoloji_articles.rss","xml","item","title")
# getData("https://www.trthaber.com/spor_articles.rss","xml","item","title")
# getData("https://www.haberimizvar.net/rss/siyaset.xml","xml","item","title")
# getData("https://www.noktahaber.com.tr/rss/siyaset.xml","xml","item","title")
# getData("https://www.noktahaber.com.tr/rss/saglik.xml","xml","item","title")
# getData("https://www.haberankara.com/rss/categorynews/teknoloji","xml","item","title")
# getData("https://www.haberankara.com/rss/categorynews/spor","xml","item","title")
# getData("https://www.sozcu.com.tr/feeds-haberler","html.parser","item","title")
# getData("https://www.ntv.com.tr/son-dakika.rss","xml","entry","title")
# getData("https://www.milliyet.com.tr/rss/rssnew/dunyarss.xml","xml","item","title")
# getData("https://www.haberturk.com/rss","xml","item","title")
# getData("https://sputniknews.com.tr/export/rss2/archive/index.xml","xml","item","title")
# getData("https://www.ntv.com.tr/spor.rss","xml","entry","title")
# getData("https://www.ntv.com.tr/ekonomi.rss","xml","entry","title")
# getData("https://www.ntv.com.tr/teknoloji.rss","xml","entry","title")
# getData("https://www.ntv.com.tr/saglik.rss","xml","entry","title")
# getData("https://www.yeniakit.com.tr/rss/haber/siyaset","xml","item","title")
# getData("https://www.milliyet.com.tr/rss/rssnew/siyasetrss.xml","xml","item","title")



table = pd.DataFrame({"title":news})
datatoexcel = pd.ExcelWriter('teknoloji.xlsx')
table.to_excel(datatoexcel)
datatoexcel._save()


###########################   Data Preprocessing   #######################################

'''
news = []
file = open(r'CUsers\Eray\Desktop\data.csv',encoding="utf8")
csvreader = csv.reader(file)
rows = []
normalizer = Normalizer()

for row in csvreader:
    text_lower = normalizer.lower_case(row[1])
    text_without_punctuations = Normalizer.remove_punctuations(text_lower)
    cleaned_text = normalizer.remove_numbers(text_without_punctuations)
    news.append(cleaned_text.split())

print(news)  #  [['asgari', 'ücrette', 'gözler', 'toplantıda'], ['yerel', 'yönetimlere', 'milyar', 'lira', 'çevre', 'desteği'] .... ]
'''


###########################   Vectorization TF-IDF   #######################################




