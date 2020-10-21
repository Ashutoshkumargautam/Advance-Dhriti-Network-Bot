from selenium import webdriver
import datetime
import imaplib
import logging
import re
import shutil
import email
import sys
import time
import subprocess
website_reponse = 'True'
#[servername - Patner.gtel.com] server 1 username and password
s1_admin_username = 'Anil'
s1_admin_password = 'Anil2522'
#[servername - patner.gtel.conaxia] server 2 username and password
s2_admin_username = 'dhriti'
s2_admin_password = '112233'
#[servername - Patner.gtel] server 3 username and password
s3_admin_username = 'dhritinetwork'
s3_admin_password = 'dhritinetwork508'
#bot email id and password
botemail = "xyzxxxaxbxzx123@gmail.com"
botemailpassword = "xxx@123456"
#=====[Making log file here]==============================>
logging.basicConfig(filename="Dhritinetwork_Bot.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
starting_time = datetime.datetime.now()
bt = starting_time.strftime("%A"), "Date", starting_time.date(), "/", "Time", starting_time.time()
f = open('bot_time.txt', 'w')
f.write(str(bt))
f.close()
#--------------------------------------->>
f = open('server_number.txt', 'r')
server_num = f.read()
f.close()
#=============[Reading email here..]===============================>>
mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
mail.login(botemail, botemailpassword)
num_of_mail = 0
#--------------------------------->
while True:
       #=======[Loader start here]=========>>
       #2nd -> if any email is not comming in bot email box then wait  infinite time....
       print("Waitting for website response...")
       #------------------------------------------------->
       # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
       animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
       for i in range(len(animation)):
              time.sleep(0.2)
              sys.stdout.write("\r" + animation[i % len(animation)])
              sys.stdout.flush()
       print("\n")
       #======[loader end]=================================================>
       mail.select('INBOX')
       typ, data = mail.search(None, "UNSEEN")
       mail_ids = data[0]
       id_list = mail_ids.split()
       if len(id_list) > num_of_mail:
              # ================================================================================>>
              # 1st -> if any new comes than read that email store
              f = open("test_1.txt", "w")
              f.write("true")
              f.close()
              f = open("test_1.txt", "r")
              website_response = f.read()
              for i in reversed(id_list):
                     type, data = mail.fetch(i, '(RFC822)')

                     for response_part in data:
                            if isinstance(response_part, tuple):
                                   msg = email.message_from_string(response_part[1].decode('utf-8', errors='ignore'))
              num_of_mail = len(id_list)
              # ========[condition here]==========================================================================================>>
              if website_response == 'true':
                     # =====[Email reading here....]===========>>
                     imap_server = imaplib.IMAP4_SSL(host='imap.gmail.com')
                     imap_server.login('xyzxxxaxbxzx123@gmail.com', 'xxx@123456')
                     imap_server.select()  # Default is `INBOX`
                     _, message_numbers_raw = imap_server.search(None, 'ALL')
                     for message_number in message_numbers_raw[0].split():
                            _, msg = imap_server.fetch(message_number, '(RFC822)')
                            x = msg[0][1]
                            f = open('mail_data_file.txt', 'w')
                            f.write(str(x))
                            f.close()
                            with open('mail_data_file.txt', 'r') as file:
                                   for line in file:
                                          for word in line.split():
                                                 # reading the file writting splited word inside the text file.
                                                 f = open("test.txt", "w")
                                                 # ignoring the html here....
                                                 v = word
                                                 result = re.sub("<.|/\'*?>", "", v)
                                                 clean = result
                                                 f.write(clean)
                                                 f.close()
                                          #=========================>
                                          string = open('test.txt').read()
                                          new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
                                          open('test1.txt', 'w').write(new_str)
                                          #=============>>
                                          with open('test1.txt', 'r') as f:
                                                 for line in f:
                                                        username = line.split(' ')[0]
                                                        f = open('username.txt', 'w')
                                                        f.write(username)
                                                        f.close()
                                                        f = open('username.txt', 'r')
                                                        clientname = f.read()
                                                        print(clientname)
                                                        # Reading mail data for server umber detect and take action acc. to the server number.
                                                        with open('mail_data_file.txt', 'r') as file:
                                                            for line in file:
                                                                for part in line.split():
                                                                    if "Server:" in part:
                                                                        f = open('s1.txt', 'w')
                                                                        f.write(part)
                                                                        f.close()
                                                        string = open('s1.txt').read()
                                                        new_str = re.sub('[^a-zA-Z0-9\n\r\.]', ' ', string)
                                                        open('s2.txt', 'w').write(new_str)
                                                        with open('s2.txt', 'r') as f:
                                                            for line in f:
                                                                server_num = line.split(' ')[7]
                                                                f = open('server_number.txt', 'w')
                                                                f.write(server_num)
                                                                f.close()
                                                                f = open('server_number.txt', 'r')
                                                                server_number = f.read()
                                                                print(server_number)
                                                        # =========================================================>>
                                                        if server_num == '1':
                                                            print("This is server 1")
                                                            print("Username --> ", s1_admin_username, "|" "Password --> ", s1_admin_password)
                                                            # ---------------------------------------------------------------------------->
                                                            driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")
                                                            driver.get('https://partner.gtel.in/Partner/Default.aspx')
                                                            time.sleep(0.10)
                                                            # ============[Bot is click and input the username here]================>>>
                                                            driver.find_element_by_xpath('//*[@id="txtUserName"]').click()
                                                            driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(s1_admin_username)
                                                            # ============[Bot is click and input the Password here]================>>>
                                                            driver.find_element_by_xpath('//*[@id="txtPassword"]').click()
                                                            driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(s1_admin_password)
                                                            # ============[Bot is now clicking on login button to login in the website]====>>>
                                                            driver.find_element_by_xpath('//*[@id="save"]').click()
                                                            # =======[ Now bot is trying to all user account ]=====================>>>
                                                            driver.get('https://partner.gtel.in/Partner/Accounts.aspx')
                                                            time.sleep(0.10)
                                                            # ======[ Now bot is trying to click search bar   ]===============================>>>
                                                            driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtserch"]').click()
                                                            # ======[ Now bot is trying type on search bar  ]==============================================>>
                                                            driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtserch"]').send_keys(clientname)
                                                            time.sleep(1)
                                                            # ======[click on search button]===========================================>
                                                            driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnserch"]').click()
                                                            time.sleep(1)
                                                            # ================[Bot is trying to click on renew plan]=======================================>>>
                                                            popup = driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/div[1]/div[1]/table/tbody/tr/td[2]/div[1]/div/div/table/tbody/tr[2]/td[12]/input').click()
                                                            time.sleep(1)
                                                            # ==============[Scroll here this gonna be easy]=========================================>>>
                                                            scr1 = driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/div[1]/div[3]')
                                                            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight" ,scr1)
                                                            time.sleep(1)
                                                            # --[Bot is clicking on cancel button on popup-->>
                                                            driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/div[1]/div[3]/table/tbody/tr[40]/td/button[2]').click()
                                                            time.sleep(1)
                                                            # ============[This is reporting section start here]===============================>>>
                                                            driver.save_screenshot("user_status.png")
                                                            logger.info(" [+] Screenshot taken successfully")
                                                            # ===========[Now moving to another folder screenshot for managing space to next screenshot]=======>>
                                                            original = r'C:/Users/Perfect TC Society/PycharmProjects/Dhritinetwork_Bot/user_status.png'
                                                            target = r'C:/Users/Perfect TC Society/PycharmProjects/Dhritinetwork_Bot/db/user_status.png'
                                                            shutil.move(original, target)
                                                            # ===========[All Task Complete successfully logout now..]=======>>
                                                            driver.find_element_by_xpath('//*[@id="lbklogout"]').click()
                                                            time.sleep(0.10)
                                                            logger.info(" [+] Successfully task completed Now.")
                                                            logger.info(" [+] Closing entire browser")
                                                            """ Here Bot is trying close entire browser """
                                                            driver.close()
                                                            # ---------------------------------------------------------------------------->
                                                        elif server_num == '2':
                                                            print("This is server 2")
                                                            print("Username  --> ", s2_admin_username, "|" "Password  --> ", s2_admin_password)
                                                            # ----------------------------------------------------------------------------------->
                                                            driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")
                                                            driver.get('https://partner.gtel.in/Partner/Default.aspx')
                                                            time.sleep(0.10)
                                                            # ============[Bot is click and input the username here]================>>>
                                                            driver.find_element_by_xpath('//*[@id="txtUserName"]').click()
                                                            driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(s1_admin_username)
                                                            # ============[Bot is click and input the Password here]================>>>
                                                            driver.find_element_by_xpath('//*[@id="txtPassword"]').click()
                                                            driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(s1_admin_password)
                                                            # ============[Bot is now clicking on login button to login in the website]====>>>
                                                            driver.find_element_by_xpath('//*[@id="save"]').click()
                                                            # =======[ Now bot is trying to all user account ]=====================>>>
                                                            driver.get('https://partner.gtel.in/Partner/Accounts.aspx')
                                                            time.sleep(0.10)
                                                            # ======[ Now bot is trying to click search bar   ]===============================>>>
                                                            driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtserch"]').click()
                                                            # ======[ Now bot is trying type on search bar  ]==============================================>>
                                                            driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtserch"]').send_keys(clientname)
                                                            time.sleep(1)
                                                            # ======[click on search button]===========================================>
                                                            driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnserch"]').click()
                                                            time.sleep(1)
                                                            # ================[Bot is trying to click on renew plan]=======================================>>>
                                                            popup = driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/div[1]/div[1]/table/tbody/tr/td[2]/div[1]/div/div/table/tbody/tr[2]/td[12]/input').click()
                                                            time.sleep(1)
                                                            # ==============[Scroll here this gonna be easy]=========================================>>>
                                                            scr1 = driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/div[1]/div[3]')
                                                            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                                                            time.sleep(1)
                                                            # --[Bot is clicking on cancel button on popup-->>
                                                            driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/div[1]/div[3]/table/tbody/tr[40]/td/button[2]').click()
                                                            time.sleep(1)
                                                            # ============[This is reporting section start here]===============================>>>
                                                            driver.save_screenshot("user_status.png")
                                                            logger.info(" [+] Screenshot taken successfully")
                                                            # ===========[Now moving to another folder screenshot for managing space to next screenshot]=======>>
                                                            original = r'C:/Users/Perfect TC Society/PycharmProjects/Dhritinetwork_Bot/user_status.png'
                                                            target = r'C:/Users/Perfect TC Society/PycharmProjects/Dhritinetwork_Bot/db/user_status.png'
                                                            shutil.move(original, target)
                                                            # ===========[All Task Complete successfully logout now..]=======>>
                                                            driver.find_element_by_xpath('//*[@id="lbklogout"]').click()
                                                            time.sleep(0.10)
                                                            logger.info(" [+] Successfully task completed Now.")
                                                            logger.info(" [+] Closing entire browser")
                                                            """ Here Bot is trying close entire browser """
                                                            driver.close()
                                                            #-------------------------------------------------------------------------------------->
                                                            print("This is server 2")
                                                            print("Username  --> ", s2_admin_username, "|" "Password  --> ", s2_admin_password)
                                                            # ----------------------------------------------------------------------------------->
                                                            driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")
                                                            driver.get('https://partner.gtel.in/Partner/Default.aspx')
                                                            time.sleep(0.10)
                                                            # ============[Bot is click and input the username here]================>>>
                                                            driver.find_element_by_xpath('//*[@id="txtUserName"]').click()
                                                            driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(s1_admin_username)
                                                            # ============[Bot is click and input the Password here]================>>>
                                                            driver.find_element_by_xpath('//*[@id="txtPassword"]').click()
                                                            driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(s1_admin_password)
                                                            # ============[Bot is now clicking on login button to login in the website]====>>>
                                                            driver.find_element_by_xpath('//*[@id="save"]').click()
                                                            # =======[ Now bot is trying to all user account ]=====================>>>
                                                            driver.get('https://partner.gtel.in/Partner/Accounts.aspx')
                                                            time.sleep(0.10)
                                                            # ======[ Now bot is trying to click search bar   ]===============================>>>
                                                            driver.find_element_by_xpath( '//*[@id="ContentPlaceHolder1_txtserch"]').click()
                                                            # ======[ Now bot is trying type on search bar  ]==============================================>>
                                                            driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtserch"]').send_keys(clientname)
                                                            time.sleep(1)
                                                            # ======[click on search button]===========================================>
                                                            driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnserch"]').click()
                                                            time.sleep(1)
                                                            # ================[Bot is trying to click on renew plan]=======================================>>>
                                                            popup = driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/div[1]/div[1]/table/tbody/tr/td[2]/div[1]/div/div/table/tbody/tr[2]/td[12]/input').click()
                                                            time.sleep(1)
                                                            # ==============[Scroll here this gonna be easy]=========================================>>>
                                                            scr1 = driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/div[1]/div[3]')
                                                            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                                                            time.sleep(1)
                                                            # --[Bot is clicking on cancel button on popup-->>
                                                            driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/div[1]/div[3]/table/tbody/tr[40]/td/button[2]').click()
                                                            time.sleep(1)
                                                            # ============[This is reporting section start here]===============================>>>
                                                            driver.save_screenshot("user_status.png")
                                                            logger.info(" [+] Screenshot taken successfully")
                                                            # ===========[Now moving to another folder screenshot for managing space to next screenshot]=======>>
                                                            original = r'C:/Users/Perfect TC Society/PycharmProjects/Dhritinetwork_Bot/user_status.png'
                                                            target = r'C:/Users/Perfect TC Society/PycharmProjects/Dhritinetwork_Bot/db/user_status.png'
                                                            shutil.move(original, target)
                                                            # ===========[All Task Complete successfully logout now..]=======>>
                                                            driver.find_element_by_xpath('//*[@id="lbklogout"]').click()
                                                            time.sleep(0.10)
                                                            logger.info(" [+] Successfully task completed Now.")
                                                            logger.info(" [+] Closing entire browser")
                                                            """ Here Bot is trying close entire browser """
                                                            driver.close()
                                                            #-------------------------------------------------------------------------------------->
                                                        else:
                                                            logger.info(" [+] Excuting main file now.. ")
                                                            subprocess.call("python main.py")
                                                            #========[Deleting new email from inbox]===========================>
                                                            box = imaplib.IMAP4_SSL('imap.gmail.com', 993)
                                                            box.login(botemail, botemailpassword)
                                                            box.select('Inbox')
                                                            typ, data = box.search(None, 'ALL')
                                                            for num in data[0].split():
                                                                box.store(num, '+FLAGS', '\\Deleted')
                                                            box.expunge()
                                                            box.close()
                                                            box.logout()
                                                            logger.info(" [+] New Email is Deleted. ")
                                                            #============[finishing up logging ]================================>>
                                                            #=======[The creadit Section from developer]========================>>>
                                                            logger.info(" [+] Dhritinetwork_Bot - Version 1.0")
                                                            logger.info(" [+] Made By : Ashutosh kumar Gautam")
                                                            logger.info(" [+] Contact me : Email - ashutoshkumargautam@protonmail.com")
                                                            logger.info(" <-- [+] Closing Date and Time  ")
                                                            logger.info("Back in infinite now...")
                                                            print(" [+] Back in infinite loop now...")
                                                            logger.info("[======================================================================================>")
                                                            subprocess.call("python main.py", shell=True)
              subprocess.call("python main.py", shell=True)
       continue
