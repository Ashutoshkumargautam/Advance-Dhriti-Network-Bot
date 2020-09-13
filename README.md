# Advance-Dhriti-Network-Bot
---------------------------------

#!/usr/bin/env python3
""" Here i am importing modules """
from selenium import webdriver

""" Starting making Dhritinetwork_Bot """
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com")# Here i Dhritinet_Bot is trying to open chrome browser """
print("driver.title")
driver.quite()  # Dhritinet_Bot is trying to close entire browser
