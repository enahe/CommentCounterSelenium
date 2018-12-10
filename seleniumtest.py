from selenium import webdriver
import time
from collections import Counter
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='PuddingFace', api_key='Kcyqp3F6BrMxx3Gj08KL')
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

linkList = browser.find_elements_by_class_name('UFIPagerLink')
for links in linkList:
    browser.execute_script("arguments[0].click();", links)


nameBrowser = browser.find_elements_by_class_name(' UFICommentActorName')
nameList = []
countList = []
properNameList = []

for names in nameBrowser:
    nameList.append(names.text)
    print names.text
nameCount = Counter(nameList)
print nameCount
for counters in nameCount:
    properNameList.append(counters)
    countList.append(nameCount[counters])
print properNameList
print countList
data = [go.Bar(
            x=properNameList,
            y=countList
    )]

py.plot(data, filename='LLCU 352 Attendance Graph')

