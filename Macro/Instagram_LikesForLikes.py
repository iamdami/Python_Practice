from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

driver = webdriver.Chrome("<put Chrome driver path>")

URL = "https://www.instagram.com/"
driver.get(URL)

my_id = "<put id>"
driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[1]/div/label/input""").send_keys(my_id)

my_pw = "<put pw>"
driver.find_element_by_name("""//*[@id="loginForm"]/div/div[2]/div/label/input""").send_keys(my_pw)

# Login button click
driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[3]""").click()
time.sleep(3)

# Do like
likes = driver.find_element_by_xpath("//article/div[3]/section[1]/span[1]/button")
likes.send_keys(Keys.ENTER)

for i in range(10):
    next_context = driver.find_element_by_css_selector("boby > div.2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow")
    next_context.click()

    time.sleep(random.randrange(3, 6, 5))

# Do like
    likes = driver.find_element_by_xpath("//article/div[3]/section[1]/span[1]/button")
    likes.send_keys(Keys.ENTER)
