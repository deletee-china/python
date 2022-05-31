import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import requests
import os

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
headers = {
'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}
url = 'https://www.zxzjtv.com/detail/3748.html'
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(executable_path='./chromedriver',
                          options=option,
                          chrome_options=chrome_options)
driver.get(url)
os.mkdir("../新蝙蝠侠")
li_list = driver.find_elements(By.XPATH,
                               "/html/body/div[1]/div/div/div/div/ul[1]/li/a")
length = len(li_list)
print(li_list)

for i in range(0, length):
    li_list = driver.find_elements(
        By.XPATH, "/html/body/div[1]/div/div/div/div/ul[1]/li/a")
    link = li_list[i]
    url = link.get_attribute('href')
    mp4_name = link.text
    print(url, mp4_name)
    driver.get(url)
    time.sleep(1)
    driver.switch_to.frame(2)
    mp4_src = driver.find_element(By.XPATH,'//div[@class="dplayer-video-wrap"]/video')
    mp4_src2 = mp4_src.get_attribute('src')
    print(mp4_src2)
    print("正在在下")
    response=requests.get(mp4_src2,headers=headers).content
    sss = "../新蝙蝠侠/" + mp4_name + '.mp4'
    with open(sss, 'wb') as f:
        f.write(response)
    print(mp4_name + "下载完成")
    driver.back()
'''
def get_url():
    driver.get(url)
    driver_btn=driver.find_element(By.PARTIAL_LINK_TEXT,"朕已阅")
    driver_btn.click()
    driver_inconfot=driver.find_element(By.CLASS_NAME,value='iconfont').click()
    driver_inconfot.click()
def search_data(data):
     search_input=driver.find_element(By.ID,"wd")
     search_input.send_keys('1234')
     search_s=driver.find_element(By.ID,'searchbutton')
     search_s.click()

if __name__=='__main__':
        get_url()
        search_data("美剧")


'''
'''
option= ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
url='https://www.zxzjtv.com/video/102-1-23.html'
driver = webdriver.Chrome(executable_path='./chromedriver ', options=option)
driver.get(url)
sleep(0.4)
driver.switch_to.frame(2)
print(driver.page_source)
mp4_src=driver.find_element(By.XPATH,'//div[@class="dplayer-video-wrap"]/video')
mp4_src2=mp4_src.get_attribute('src')

print(mp4_src2)
'''
'''
with open ('老友记2.mp4','wb')as f:
f.write(r)
print('下载成功')'''
