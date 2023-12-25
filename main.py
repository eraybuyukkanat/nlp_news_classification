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
datatoexcel = pd.ExcelWriter('data.xlsx')
table.to_excel(datatoexcel)
datatoexcel._save()


###########################   Data Preprocessing   #######################################

news = []
file = open(r'C:\Users\Eray\Desktop\data.csv',encoding="utf8")
csvreader = csv.reader(file)
rows = []
normalizer = Normalizer()

for row in csvreader:
    text_lower = normalizer.lower_case(row[1])
    text_without_punctuations = Normalizer.remove_punctuations(text_lower)
    cleaned_text = normalizer.remove_numbers(text_without_punctuations)
    news.append(cleaned_text.split())

print(news)  #  [['asgari', 'ücrette', 'gözler', 'toplantıda'], ['yerel', 'yönetimlere', 'milyar', 'lira', 'çevre', 'desteği'] .... ]



###########################   Vectorization TF-IDF   #######################################

# ..................
