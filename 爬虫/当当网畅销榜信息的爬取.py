import csv
import time
from time import sleep
from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import requests
import os
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(executable_path='./chromedriver', options=option,chrome_options=chrome_options)
url='http://search.dangdang.com/?key=%B3%A9%CF%FA%B0%F1&act=input'
driver.get(url)
js = 'window.scrollBy(0,8000)'
driver.execute_script(js)
sleep(1)

driver.execute_script(js)
for page in range(5):
        li_list=driver.find_elements(By.XPATH,'//ul[@class="bigimg"]/li')
        #print(li_list)
        length=len(li_list)
        for li in range(0,length):
            li_list = driver.find_elements(By.XPATH, '//ul[@class="bigimg"]/li')
            link=li_list[li]
            book_name=link.find_element(By.XPATH,'.//p[@class="name"]/a').text
            book_name=book_name.split(" ")[0]
            print(book_name)
            book_price=link.find_element(By.XPATH,'.//span[@class="search_now_price"]').text
            print(book_price)
            book_write = link.find_element(By.XPATH, './/p[@class="search_book_author"]/span').text
            print(book_write)
            book_aut=link.find_element(By.XPATH,'.//p[@class="search_book_author"]/span[3]').text
            book_aut=book_aut.replace('/','')
            print(book_aut)
            with open('当当畅销榜信息.csv','a',encoding='utf-8')as f:
                csv_write=csv.writer(f)
                csv_write.writerow([book_name,book_price,book_write,book_aut])
        nextPage = driver.find_element(By.LINK_TEXT,"下一页")
        driver.execute_script("arguments[0].click();",nextPage)
        sleep(1)