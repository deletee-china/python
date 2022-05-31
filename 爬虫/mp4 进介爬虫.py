import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import requests
import os
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}
url='https://v3-default.ixigua.com/4fd935e9bd76c8ffc28113df5638bd03/628778de/video/tos/cn/tos-cn-v-6f4170/f9d03350bbe24119b153836c4dfb3774/?tg=TG@yhzyw&filename=1.mp4'
response=requests.get(url,headers=headers).content
print(response)
