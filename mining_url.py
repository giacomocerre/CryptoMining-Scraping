import json
import csv
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.cryptocompare.com/mining/#/equipment")
assert "Crypto" in driver.title

### Scrollin to bottom and wait
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")
###Create CSV
url_csv = open("url.csv", "w")
### Loop for infinite page scroll
while True:
    ### Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    ### Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    ### Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    ### Break condition
    if new_height == last_height:
        ### Get the xpath of the info
        urls  = driver.find_elements_by_xpath("//mining-list/div[1]/div[@class='item-list list-mining shadowed list-sponsorship-enabled ng-scope']/div/div[2]/h3/a")
        for url in urls:
            url_csv.write(url.get_attribute('href') + '\n')
        break
    last_height = new_height