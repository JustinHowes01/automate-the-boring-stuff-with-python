from selenium import webdriver
from time import sleep

browser = webdriver.ChromiumEdge()
browser.get('https://automatetheboringstuff.com')
elem = browser.find_element(by='css selector', value='body > div > main > div > ul:nth-child(19) > li:nth-child(1) > a')
elem.click()
elem = browser.find_element(by='css selector', value='#calibre_link-1609 > p')
print(elem.text)
sleep(5)
browser.back()
sleep(5)
