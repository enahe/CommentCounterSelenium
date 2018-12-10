from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path=r"C:/Users/Tommy/chromedriver_win32/chromedriver.exe", chrome_options=option)
browser.get("http://www.facebook.com")

browser.find_element_by_id("email").clear()
browser.find_element_by_id("email").send_keys("bbjoe345@gmail.com")
browser.find_element_by_id("pass").clear()
browser.find_element_by_id("pass").send_keys("Sandvich12")
browser.find_element_by_id("loginbutton").click()
time.sleep(10)
browser.get("https://www.facebook.com/groups/479270829257357/")
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=True
nameList = browser.find_elements_by_class_name(' UFICommentActorName')

for names in nameList:
    print names.text
