import json
import csv
import time
import re
from selenium import webdriver

driver = webdriver.Chrome()
with open('mining_eqp_2.csv', mode='w') as mining:
    with open('url.txt', 'r') as f:
        for url in f:
            driver.get(url)
            assert "Crypto" in driver.title
            ###XPATH
            names       = driver.find_elements_by_xpath("//h1[@class='page-title']/span[1]")
            equips      = driver.find_elements_by_xpath("//h1[@class='page-title']/span[2]")
            prices      = driver.find_elements_by_xpath("//li[@class='price']/span[2]/span[1]")
            powers      = driver.find_elements_by_xpath("//mining-equipment-summary/div/div[1]/div[1]/div[2]/span")
            h_rates     = driver.find_elements_by_xpath("//mining-equipment-summary/div/div[1]/div[2]/div[2]/span[1]")
            GH_s        = driver.find_elements_by_xpath("//mining-equipment-summary/div/div[1]/div[2]/div[2]/span[2]")
            values      = driver.find_elements_by_xpath("//mining-equipment-summary/div/div[1]/div[3]/div[2]/a/span")
            day_costs   = driver.find_elements_by_xpath("//mining-equipment-summary/div/div[2]/div[1]/div[2]/span")
            r_day       = driver.find_elements_by_xpath("//mining-equipment-summary/div/div[2]/div[2]/div[2]/span")
            r_week      = driver.find_elements_by_xpath("//mining-equipment-summary/div/div[3]/div[1]/div[2]/span")
            r_month     = driver.find_elements_by_xpath("//mining-equipment-summary/div/div[3]/div[2]/div[2]/span")
            r_year      = driver.find_elements_by_xpath("//mining-equipment-summary/div/div[3]/div[3]/div[2]/span")
            day_payback = driver.find_elements_by_xpath("//mining-equipment-summary/div/div[4]/div[2]/div[2]/span")
            annual_pr   = driver.find_elements_by_xpath("//mining-equipment-summary/div/div[4]/div[3]/div[2]/span")
            user_rating = driver.find_elements_by_xpath("//average-rating/div/div[1]/div[1]/span[1]")
            ### for in zip for single element and get our text
            for nm, eqp, prc, pwr, hr, ghs, val, dc, day, week, month, year, pay, ann, rating in zip(names, equips, prices, powers, h_rates, GH_s, values, day_costs, r_day, r_week, r_month, r_year, day_payback, annual_pr, user_rating):
                release   = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[3]/div[2]/div/div[1]/div[1]/table/tbody/tr[3]/td[2]")
                if release:
                    release_date = release[0].text
                    print(release_date)
                else:
                    release_date = "---"
                    print(release_date)
                price     = prc.text.replace(',', '')
                h_rate    = hr.text.replace(',', '').replace('.', ',') + " " + ghs.text
                day_cost  = dc.text.replace(',','').replace('.',',')
                annual = ann.text+'%'
                mining_writer = csv.writer(mining, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                mining_writer.writerow([nm.text, eqp.text, price, pwr.text, h_rate, val.text, day_cost, day.text, week.text, month.text, year.text, pay.text, annual, release_date, rating.text])
            