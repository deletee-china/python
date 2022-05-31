from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
bro= webdriver.Chrome(executable_path='./chromedriver')
bro.get('http://www.taobao.com')
#标签定位
search_input=bro.find_element(By.ID,'q')
search_input.send_keys('Iphone')

#执行一组js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')#滚动
sleep (2)
btn= bro.find_element(By.CLASS_NAME,'tb-bg')
btn.click()


bro.get('https://www.baidu.com')
sleep(2)
#回退
bro.back()
sleep(2)
bro.forward()
#前进
sleep(5)
bro.quit()
# 发起请求:get(url)
# 标签的定位find系列的方法
# 标签的交互:send_key('xxx')
# 执行js程序:excute_script('jscode')
# 前进和后退: forward(),back()
# 关闭浏览器: quit()
# selenium处理iframe