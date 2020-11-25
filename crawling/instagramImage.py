from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time

keyword = "손흥민"
url = "https://www.instagram.com/explore/tags/{}".format(keyword)

driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get(url)

time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html)

insta = soup.select(".v1Nh3.kIKUG._bz0w")
n= 1
for i in insta:
    print("https://www.instagram.com/"+i.a["href"])
    SonUrl = i.select_one(".KL4Bh").img["src"]
    with urlopen(SonUrl) as f:
        with open("./son" + keyword + str(n) + ".jpg", "wb") as h:
            img = f.read()
            h.write(img)
        n += 1
        print(SonUrl)
        print()

driver.close()
