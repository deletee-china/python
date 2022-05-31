import csv
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import requests
import os

headers = {
    'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'cookie':
    'douyin.com; ttwid=1|6CaTz_5UmPTwIvqFcShveji03dWmhb4oucXD6k9uUfU|1651233570|75d6be4a5e908bed75996053b174417203c6ba1d283a54a282bff06d71496765; passport_csrf_token=e7d431cd73802cb9eb1daa7dff977246; passport_csrf_token_default=e7d431cd73802cb9eb1daa7dff977246; s_v_web_id=verify_l2kdu61c_pThjMyCr_4MHY_4JVI_8xzc_NTsHK4cCQ2Kt; AVATAR_FULL_LOGIN_GUIDE_ITA_TIMESTAMP=1651233574398; AVATAR_FULL_LOGIN_GUIDE_ITA_COUNT=1; odin_tt=f2e86aec662809255e98c66f2f360c3907cc489ac10f0b6caece113e00c4a3cba516f7933f091935d0bfe5d48437381bd5c7f3c93712aa0ca7b30fa8813a7d54; _tea_utm_cache_2285=undefined; THEME_STAY_TIME=299543; IS_HIDE_THEME_CHANGE=1; pwa_guide_count=3; _tea_utm_cache_2018=undefined; __ac_nonce=06283b2bb006ebd7258ee; __ac_signature=_02B4Z6wo00f01evQiVAAAIDAkx5iVR35Fdnr8I3AABh5dy7uT70IQV8iGyzHr9bzRcA9RMUKRuCwH0cT2wH-j6SXj8MVyoiZMJSW0bi7OIaBKokoGlX7LMSrAncarGC9PXAB1i2cCtDfpwMB26; douyin.com; strategyABtestKey=1652798144.294; AB_LOGIN_GUIDE_TIMESTAMP=1652798144233; _tea_utm_cache_6383=undefined; _tea_utm_cache_1300=undefined; msToken=eFLG81ht4OfjnfH_0SJgJl9iGs6M9kOP9s_1bYRt-BRpZloyTMByTkIZ41Dv89Y2ZGKbINETLvDqYENVTiP1br1aBpRp-DO7odyw6jlMXeIX5rhh82gvMtth5h-jefA=; home_can_add_dy_2_desktop=1; msToken=gG8Wu4JDZfHDlD2cFDTqc4wb6OLNghypc_N2Xua64itmS9Pm2gcz6bly6WyeL0Q5ljqFdBJEIP7gHYpOFAcvFjcKiJphniWIL1Mb0Q9L2dkid1Gib-7ptYs6Gy3W1a4=; tt_scid=RUCbp9pbeeRPZVNB4gKpEjUUWJmuenAonmiMXfZhKcwMD13Akdx9VbY-aqX-sIRw1d90'
}
url = 'https://www.douyin.com/video/7096776037283007781'
response = requests.get(headers=headers, url=url)
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(executable_path='./chromedriver ', options=option)
#                         chrome_options=chrome_options)
driver.get(url=url)
title = driver.find_element(
    By.XPATH,
    '//*[@id="root"]/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div[1]/div/h1/span[2]/span[1]/span/span/span'
).text
print(title)
#title = re.findall('<title>(.*?)</title>', response.text)
#print(title)
