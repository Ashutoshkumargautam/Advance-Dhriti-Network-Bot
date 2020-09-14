# Advance-Dhriti-Network-Bot
---------------------------------

#!/usr/bin/env python2
from selenium import webdriver
import time

driver = webdriver.Firefox(firefox_binary="/usr/bin/firefox-esr")
driver.get('https://apitandnetworksolutions.com/admin/login.php');
driver.find_element_by_xpath('/html/body/div/form/input[1]')[0].send_keys("Ashutosh kumar")
driver.find_element_by_xpath('/html/body/div/form/input[2]')[0].send_keys("12345")
# driver.find_elements_by_xpath('/html/body/div/form/input[1]')[0].send_keys("selenium bot")
# driver.find_elements_by_xpath('//*[@name="your-email"]')[0].send_keys("selenium@bot.com")
# time.sleep(3)
# time.sleep(3)
# driver.find_elements_by_xpath('//*[@value="Send"]')[0].click()
# time.sleep(3)
# driver.quit()
