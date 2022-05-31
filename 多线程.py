import time
from time import sleep
from  selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import requests
import os
headers = {
            'User-Agent':
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
        }
url='https://www.zxzjtv.com/detail/102.html'
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(executable_path='./chromedriver ', options=option)
driver.get(url)
#os.mkdir("老友记第九季")
li_list=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div/div/div/ul[1]/li/a")
length=len(li_list)
print(li_list)

for i in range(15,length):
    li_list = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div/ul[1]/li/a")
    link=li_list[i]
    url=link.get_attribute('href')
    mp4_name=link.text
    driver.get(url)
    time.sleep(1)
    driver.switch_to.frame(2)
    mp4_src=driver.find_element(By.XPATH,'//div[@class="dplayer-video-wrap"]/video')
    mp4_src2=mp4_src.get_attribute('src')
    response=requests.get(mp4_src2,headers=headers).content
    print("正在在下")
    sss="老友记第九季/"+mp4_name+'.mp4'
    with open (sss,'wb')as f:
           f.write(response)
    print(mp4_name+"下载完成")
    driver.back()