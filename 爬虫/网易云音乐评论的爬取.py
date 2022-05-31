from time import sleep
from  selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
option= ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])


chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
class YunSpider(object):

    def __init__(self,url):
        self.url=url
        self.driver=webdriver.Chrome(executable_path='./chromedriver ',options=option,chrome_options=chrome_options)
        #打开网站提取数据翻页
    def getcontent(self):
        self.driver.get(self.url)
        #先进如iframe
        self.driver.switch_to.frame(0)#0代表第一个框
        js='window.scrollBy(0,8000)'
        self.driver.execute_script(js)
        #翻页的实现
        with open("liqun_comments.csv", 'a', encoding='utf-8') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(['user_name', 'user_id','comment_time', 'comment', 'user_dianzan'])

        for page in range(254):
            selector= self.driver.find_elements(By.XPATH,'//div[@class="cmmts j-flag"]/div')

            for select in selector:
                text=select.find_element(By.XPATH,'.//div[@class="cnt f-brk"]').text
                time=select.find_element(By.XPATH,'.//div[@class="rp"]/div').text
                user_id=select.find_element(By.XPATH,'.//a')
                user_dianzan=select.find_element(By.XPATH,'.//a[@data-type="like"]').text
                user_dianzan=user_dianzan.replace("(","").replace(")","")
                if (user_dianzan==""):
                    user_dianzan=0
                user_id=user_id.get_attribute("href")
                user_touxiang=select.find_element(By.XPATH,'//a/img')
                user_touxiang=user_touxiang.get_attribute('src')
                text_split=text.split('：')
                csv_username=text_split[0]
                csv_comment=text_split[1]
                with open ("liqun_comments.csv", 'a', encoding='utf-8')as f:
                    csv_write=csv.writer(f)
                    csv_write.writerow([csv_username,user_id,user_touxiang,time,csv_comment,user_dianzan])



            #找到下一页的元素然后进行点击 获取文本连接属于模糊匹配
            nextPage=self.driver.find_element(By.PARTIAL_LINK_TEXT, "下一页")
            nextPage.click()
            sleep(1)




if __name__=='__main__':
    url='https://music.163.com/#/song?id=1855784425'
    yunSpider=YunSpider(url)
    yunSpider.getcontent()

