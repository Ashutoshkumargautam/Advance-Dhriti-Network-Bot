#!/usr/bin/env python3
""" Here i am importing modules """
from selenium import webdriver # window ---> mv chromedriver.exe /usr/local/bin
from time import sleep

""" Starting making Dhritinetwork_Bot """
class Dhritinetwork_Bot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("http://192.68.0.1/")
        sleep(2)
        """ Now we are detecting element on webpage and click on it by action  """
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]") \
            .click()
        sleep(2)