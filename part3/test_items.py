from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_add_butthon(browser):
    browser.get(link)
    #time.sleep(30)
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket")