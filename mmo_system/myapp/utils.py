from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import time


def autolike():
    driver = webdriver.Firefox(executable_path=r'/home/quan/Desktop/python/Django_mmo/mmo_system/geckodriver')
    cookies = pickle.load(open(r'/home/quan/Desktop/python/Django_mmo/mmo_system/myapp/cookie.pkl', 'rb'))
    driver.get("http://www.facebook.com")
    print(cookies)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("http://www.facebook.com")


