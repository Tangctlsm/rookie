# -*- coding:UTF-8 -*- 
from selenium import webdriver
import time
def login_wisonic(name,pwd):
#定位webdriver位置
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
#传入华声云后台管理地址
    driver.get("https://t.wisonic.cn/w/bm/#/login")
    driver.implicitly_wait(3)
#找到username输入框传入name参数
    name_element = driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div/div/input")
    name_element.send_keys(name)
#等待3s
    #driver.implicitly_wait(3)
#找到password输入框传入pwd参数
    pwd_element = driver.find_element_by_xpath(".//*[@id='app']/div/form/div[3]/div/div/input").send_keys(name)
    #driver.implicitly_wait(3)
#定位按钮元素
    button = driver.find_element_by_xpath(".//*[@id='app']/div/form/button")
#点击按钮
    button.click()
    driver.maximize_window()
    js = 'window.open("https://www.bing.com")'
    driver.execute_script(js)
    bing_handle = driver.current_window_handle
    print(bing_handle)
    time.sleep(5)
    driver.close()
login_wisonic("17879518831","17879518831")


