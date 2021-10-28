from selenium import webdriver   # 匯入 Selenium 網頁測試套件
from selenium.webdriver.common.by import By
from PIL import Image
import time                      # 匯入時間處理
import requests
import os
import io
import hashlib
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui


if __name__ == '__main__':
    wd = webdriver.Chrome('./chromedriver')  # 開啟 Chrome 瀏覽器
    wd.get('https://b2b.jourdeness.com/')

    ##登入B2B網站
    username = wd.find_element(By.XPATH,"//*[@id='name']")
    password = wd.find_element(By.XPATH,"//*[@id='session_login']/div/div/form/div[2]/input")
    time.sleep(1) #需要給一秒讓webdriver找對應元素
    username.send_keys("007429")
    password.send_keys("N225452442")
    time.sleep(1)
    wd.find_element(By.XPATH,"//*[@id='session_login']/div/div/form/div[3]/input").click()
    time.sleep(1)

    ##新增訂單，輸入兩個item，存檔
    wd.get('https://b2b.jourdeness.com/order_headers')
    time.sleep(1)
    ## 1.新增訂單
    wd.find_element(By.XPATH,"/html/body/div/div/div/div[3]/a").click()


    ##2.輸入兩個item BJ103C/BJ070C
    items = ['BJ103C','BJ070C']
    for i in range(len(items)):
        wd.find_element(By.XPATH, "//*[@id='select2-order_detail_item_id-container']").click()
        item = wd.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
        time.sleep(1)
        item.send_keys(items[i], Keys.ENTER)
        time.sleep(1)
    wd.find_element(By.XPATH, "//*[@id ='order_header_edit_title']/div/div/div/div[2]/div[5]/span/input").click()
    time.sleep(1)

    ##查詢未送出訂單,查詢剛剛新增的那筆
    last_item = wd.find_element_by_id("table_saved")
    time.sleep(1)
    class1=last_item.find_elements_by_class_name("table_filter.main-tr")
    time.sleep(1)
    class1[len(class1)-1].find_element_by_class_name("fa.fa-edit.btn-xs.btn-toggle").click()
    time.sleep(1)
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 網頁捲到最下面
    time.sleep(10)
    wd.quit()



