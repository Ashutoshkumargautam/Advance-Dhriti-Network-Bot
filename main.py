#importing libraries here...
from selenium import webdriver
import subprocess
import datetime
import imaplib
import logging
import shutil
import email
import time
import sys
import re
#=====================================================================================================
#==[Bot staring time]================================================================================
starting_time = datetime.datetime.now()
bt = starting_time.strftime("%A"), "Date", starting_time.date(), "/", "Time", starting_time.time()
f = open('bot_time.txt', 'w')
f.write(str(bt))
f.close()
#=====================================================================================================
#=====[Making log file here]==============================>
logging.basicConfig(filename="bot.log", format='%(asctime)s %(message)s', filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
logger.info("Bot started now")
#=======================================================================================================
#[servername - Patner.gtel.com] server 1 username and password
s1_admin_username = 'Anil'
s1_admin_password = 'Anil2522'
#[servername - Patner.gtel] server 2 username and password
s2_admin_username = 'dhriti'
s2_admin_password = '112233'
#[servername - patner.gtel.conaxia] server 3 username and password
s3_admin_username = 'dhritinetwork'
s3_admin_password = 'dhritinetwork508'
#======================================================================================================
# All website url list
url_1 = "https://partner.gtel.in/Partner/Default.aspx" #server_1
url_2 = "http://partner.conexiaworld.com" #server_2
url_3 = "https://partner.gtel.in/Partner/Default.aspx" #server_3
#======================================================================================================
#bot email id and password
botemail = "xyzxxxaxbxzx123@gmail.com"
botemailpassword = "xxx@123456"
#======================================================================================================
imap_url = 'imap.gmail.com'
#======================================================================================================
logger.info("Bot reading emails...")
logger.info("=====================================")
#=============[Reading email here..]===============================>>
mail = imaplib.IMAP4_SSL(imap_url, 993)
mail.login(botemail, botemailpassword)
num_of_mail = 0
#=======================================================================================================>
while True:
       #=======[Loader start here]=========>>
       #=======================================================================================>>>
       #if any email is not comming in bot email box then wait  infinite time....
       print("Waitting for website response...")
       logger.debug("bot waitting for website response  here...")
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
              logger.warning("waiting for true false")
              if website_response == 'true':
                     logger.info("condition is true now")
                     logger.info("reading email comes fro website")
                     # =====[Email reading here....]===========>>
                     # Connect to inbox
                     imap_server = imaplib.IMAP4_SSL(host='imap.gmail.com')
                     imap_server.login('xyzxxxaxbxzx123@gmail.com', 'xxx@123456')
                     #============================================================
                     imap_server.select()  # Default is `INBOX`
                     _, message_numbers_raw = imap_server.search(None, 'ALL')
                     for message_number in message_numbers_raw[0].split():
                            _, msg = imap_server.fetch(message_number, '(RFC822)')
                            x = msg[0][1]
                            #============================================================
                            logger.debug("making a file mail_data_file.txt")
                            f = open('mail_data_file.txt', 'w')
                            f.write(str(x))
                            logger.info("writting in file")
                            f.close()
                            #============================================================
                            logger.info("opening a mail_date_file.txt and reading and cleaing now")
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
                                          logger.info("writing a one more file called test.txt")
                                          string = open('test.txt').read()
                                          new_str = re.sub('[\r\n\']', ' ', string)
                                          logger.info("writing a one more file called test1.txt")
                                          open('test1.txt', 'w').write(new_str)
                                          #reamoving \r\n\ =====================>
                                          f = open('test1.txt')
                                          for line in f.readlines():
                                                 line = line[:-2].replace('\\r\\', '')
                                                 print(repr(line))
                                                 # =====================>
                                                 logger.info("writing a one more file called test2.txt")
                                                 f = open('test2.txt', 'w')
                                                 f.write(repr(line))
                                                 f.close()
                                                 # =============================>
                                                 logger.info("reading test2.txt")
                                                 string = open('test2.txt').read()
                                                 new_str = re.sub('[^a-zA-Z0-9\n\.]', '', string)
                                                 logger.info("opening username.txt file")
                                                 open('username.txt', 'w').write(new_str)
                                          #======================================>>
                                                 logger.info("opening username.txt file agin")
                                                 f = open('username.txt', 'r')
                                                 clientname = f.read()
                                                 print("Client Name -->", clientname)
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
                                                                      print("Server Number -->", server_number)
                                                                      logger.info(" this is server number")
                                                                      #=========================================================>>
                                                                      #===[This is server [1]====>>
                                                                      if server_num == '1':
                                                                             logger.debug("Server one is accessed")
                                                                             print("This is server 1")
                                                                             print("Username --> ", s1_admin_username,  "|" "Password --> ", s1_admin_password)
                                                                             # ---------------------------------------------------------------------------->
                                                                             logger.debug("insitining firefox webdriver now")
                                                                             driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")
                                                                             driver.get(url_1)
                                                                             logger.info("driver is searching for server 1 url")
                                                                             time.sleep(0.10)
                                                                             # ============[Bot is click and input the username here]================>>>
                                                                             logger.info("logining in website")
                                                                             driver.find_element_by_xpath('//*[@id="txtUserName"]').click()
                                                                             driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(s1_admin_username)
                                                                             # ============[Bot is click and input the Password here]================>>>
                                                                             driver.find_element_by_xpath( '//*[@id="txtPassword"]').click()
                                                                             driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(s1_admin_password)
                                                                             # ============[Bot is now clicking on login button to login in the website]====>>>
                                                                             driver.find_element_by_xpath('//*[@id="save"]').click()
                                                                             logger.info("successfully logged in")
                                                                             # =======[ Now bot is trying to all user account ]=====================>>>
                                                                             driver.get('https://partner.gtel.in/Partner/Accounts.aspx')
                                                                             time.sleep(0.10)
                                                                             # ======[ Now bot is trying to click search bar   ]===============================>>>
                                                                             driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtserch"]').click()
                                                                             # ======[ Now bot is trying type on search bar  ]==============================================>>
                                                                             logger.info("Now client name writting in search bar")
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
                                                                             # --[Bot is clicking on save button on popup-->>
                                                                             driver.find_element_by_xpath('//*[@id="btnPurchaseRenewPlanClose"]').click()
                                                                             time.sleep(1)
                                                                             logger.info("recharge done successfully.")
                                                                             # ============[This is reporting section start here]===============================>>>
                                                                             driver.save_screenshot("user_status.png")
                                                                             logger.info(" [+] Screenshot taken successfully")
                                                                             # ===========[Now moving to another folder screenshot for managing space to next screenshot]=======>>
                                                                             original = r'C:/Users/Dhritinet/PycharmProjects/Dhritinetwork_Bot/user_status.png'
                                                                             target = r'C:/Users/Dhritinet/PycharmProjects/Dhritinetwork_Bot/db/user_status.png'
                                                                             shutil.move(original, target)
                                                                             # ===========[All Task Complete successfully logout now..]=======>>
                                                                             driver.find_element_by_xpath('//*[@id="lbklogout"]').click()
                                                                             time.sleep(0.10)
                                                                             logger.info( " [+] Successfully task completed Now.")
                                                                             logger.info(" [+] Closing entire browser")
                                                                             """ Here Bot is trying close entire browser """
                                                                             driver.close()
                                                                             # ========[Deleting new email from inbox]===========================>
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
                                                                             logger.info("Successfully server 1 recharge done.")
                                                                             logger.info("Back in infinity loop")
                                                                             # ============[finishing up logging ]================================>>
                                                                             # =================================================================>
                                                                             import smtplib
                                                                             from email.mime.multipart import MIMEMultipart
                                                                             from email.mime.text import MIMEText
                                                                             from email.mime.base import MIMEBase
                                                                             from email import encoders

                                                                             fromaddr = botemail
                                                                             toaddr = "ashutoshkumargautam00000@gmail.com"

                                                                             # instance of MIMEMultipart
                                                                             msg = MIMEMultipart()

                                                                             # storing the senders email address
                                                                             msg['From'] = fromaddr

                                                                             # storing the receivers email address
                                                                             msg['To'] = toaddr

                                                                             # storing the subject
                                                                             msg['Subject'] = "Subject of the Mail"

                                                                             # string to store the body of the mail
                                                                             body = "Body_of_the_mail"

                                                                             # attach the body with the msg instance
                                                                             msg.attach(MIMEText(body, 'plain'))

                                                                             # open the file to be sent
                                                                             filename = "user_status.png"
                                                                             attachment = open("C:/Users/Dhritinet/PycharmProjects/Dhritinetwork_Bot/db/user_status.png", "rb")

                                                                             # instance of MIMEBase and named as p
                                                                             p = MIMEBase('application', 'octet-stream')

                                                                             # To change the payload into encoded form
                                                                             p.set_payload((attachment).read())

                                                                             # encode into base64
                                                                             encoders.encode_base64(p)

                                                                             p.add_header('Content-Disposition',
                                                                                          "attachment; filename= %s" % filename)

                                                                             # attach the instance 'p' to instance 'msg'
                                                                             msg.attach(p)

                                                                             # creates SMTP session
                                                                             s = smtplib.SMTP('smtp.gmail.com', 587)

                                                                             # start TLS for security
                                                                             s.starttls()

                                                                             # Authentication
                                                                             s.login(fromaddr, botemailpassword)

                                                                             # Converts the Multipart msg into a string
                                                                             text = msg.as_string()

                                                                             # sending the mail
                                                                             s.sendmail(fromaddr, toaddr, text)

                                                                             # terminating the session
                                                                             s.quit()
                                                                             # =================================================================>
                                                                             #==========================================================================>
                                                                             # ===[This is server [2]====>>
                                                                      elif server_num == '2':
                                                                             print("This is server 2")
                                                                             print("Username  --> ", s2_admin_username, "|" "Password  --> ", s2_admin_password)
                                                                             # ----------------------------------------------------------------------------------->
                                                                             driver = webdriver.Firefox( executable_path="C:\Program Files (x86)\geckodriver.exe")
                                                                             driver.get(url_2)
                                                                             time.sleep(0.10)
                                                                             # ============[Bot is click and input the username here]================>>>
                                                                             driver.find_element_by_xpath('//*[@id="txtUserName"]').click()
                                                                             driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(s2_admin_username)
                                                                             # ============[Bot is click and input the Password here]================>>>
                                                                             driver.find_element_by_xpath('//*[@id="txtPassword"]').click()
                                                                             driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(s2_admin_password)
                                                                             # ============[Bot is now clicking on login button to login in the website]====>>>
                                                                             driver.find_element_by_xpath('//*[@id="save"]').click()
                                                                             # =======[ Now bot is trying to all user account ]=====================>>>
                                                                             driver.get('http://partner.conexiaworld.com/Partner/Accounts.aspx')
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
                                                                             driver.execute_script( "arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                                                                             time.sleep(1)
                                                                             # --[Bot is clicking on cancel button on popup-->>
                                                                             driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/div[1]/div[3]/table/tbody/tr[40]/td/button[2]').click()
                                                                             time.sleep(1)
                                                                             # ============[This is reporting section start here]===============================>>>
                                                                             driver.save_screenshot("user_status.png")
                                                                             logger.info(" [+] Screenshot taken successfully")
                                                                             # ===========[Now moving to another folder screenshot for managing space to next screenshot]=======>>
                                                                             original = r'C:/Users/Dhritinet/PycharmProjects/Dhritinetwork_Bot/user_status.png'
                                                                             target = r'C:/Users/Dhritinet/PycharmProjects/Dhritinetwork_Bot/db/user_status.png'
                                                                             shutil.move(original, target)
                                                                             # ===========[All Task Complete successfully logout now..]=======>>
                                                                             driver.find_element_by_xpath('//*[@id="lbklogout"]').click()
                                                                             time.sleep(0.10)
                                                                             logger.info(" [+] Successfully task completed Now.")
                                                                             logger.info(" [+] Closing entire browser")
                                                                             """ Here Bot is trying close entire browser """
                                                                             driver.close()
                                                                             # ========[Deleting new email from inbox]===========================>
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
                                                                             # ============[finishing up logging ]================================>>
                                                                             mail_content = "Hi, Sir this is your client recharge from server 2 report from bot fo admin please check when you get time." \
                                                                                            "Thank you" \
                                                                                            "Dhritinetwork_Bot"
                                                                             sender_address = botemail
                                                                             sender_pass = botemailpassword
                                                                             receiver_address = 'ashutoshkumargautam00000@gmail.com'
                                                                             message = MIMEMultipart()
                                                                             message['From'] = sender_address
                                                                             message['To'] = receiver_address
                                                                             message['Subject'] = 'Report from Dhritinetwork_Bot for Admin'
                                                                             message.attach(MIMEText(mail_content, 'plain'))
                                                                             attach_file_name = 'C:/Users/Dhritinet/PycharmProjects/Dhritinetwork_Bot/db/user_status.png'
                                                                             attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
                                                                             payload = MIMEBase('application', 'octate-stream')
                                                                             payload.set_payload((attach_file).read())
                                                                             encoders.encode_base64(payload)  # encode the attachment
                                                                             # add payload header with filename
                                                                             payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
                                                                             message.attach(payload)
                                                                             # Create SMTP session for sending the mail
                                                                             session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
                                                                             session.starttls()  # enable security
                                                                             session.login(sender_address, sender_pass)  # login with mail_id and password
                                                                             text = message.as_string()
                                                                             session.sendmail(sender_address, receiver_address, text)
                                                                             session.quit()
                                                                             logger.info("mail sent")
                                                                             #================================================================================>
                                                                      #===[This is server [3]====>>
                                                                      if server_num == '3':
                                                                             print("This is 3rd server")
                                                                             print("Username  --> ", s3_admin_username, "|" "Password  --> ", s3_admin_password)
                                                                             #----------------------------------------------------------------------------------->
                                                                             driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")
                                                                             driver.get(url_3)
                                                                             time.sleep(0.10)
                                                                             # ============[Bot is click and input the username here]================>>>
                                                                             driver.find_element_by_xpath('//*[@id="txtUserName"]').click()
                                                                             driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(s3_admin_username)
                                                                             # ============[Bot is click and input the Password here]================>>>
                                                                             driver.find_element_by_xpath('//*[@id="txtPassword"]').click()
                                                                             driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(s3_admin_password)
                                                                             # ============[Bot is now clicking on login button to login in the website]====>>>
                                                                             driver.find_element_by_xpath('//*[@id="save"]').click()
                                                                             # =======[ Now bot is trying to all user account ]=====================>>>
                                                                             driver.get('https://partner.gtel.in/Partner/Accounts.aspx')
                                                                             time.sleep(0.10)
                                                                             # ======[ Now bot is trying to click search bar   ]===============================>>>
                                                                             driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtserch"]').click()
                                                                             # ======[ Now bot is trying type on search bar  ]==============================================>>
                                                                             logger.info("Now client name writting in search bar")
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
                                                                             driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",scr1)
                                                                             time.sleep(1)
                                                                             # --[Bot is clicking on save button on popup-->>
                                                                             driver.find_element_by_xpath('//*[@id="btnPurchaseRenewPlanClose"]').click()
                                                                             time.sleep(1)
                                                                             logger.info("recharge done successfully.")
                                                                             # ============[This is reporting section start here]===============================>>>
                                                                             driver.save_screenshot("user_status.png")
                                                                             logger.info(" [+] Screenshot taken successfully")
                                                                             # ===========[Now moving to another folder screenshot for managing space to next screenshot]=======>>
                                                                             original = r'C:/Users/Dhritinet/PycharmProjects/Dhritinetwork_Bot/user_status.png'
                                                                             target = r'C:/Users/Dhritinet/PycharmProjects/Dhritinetwork_Bot/db/user_status.png'
                                                                             shutil.move(original, target)
                                                                             # ===========[All Task Complete successfully logout now..]=======>>
                                                                             driver.find_element_by_xpath('//*[@id="lbklogout"]').click()
                                                                             time.sleep(0.10)
                                                                             logger.info(" [+] Successfully task completed Now.")
                                                                             logger.info(" [+] Closing entire browser")
                                                                             #Here Bot is trying close entire browser=========================>
                                                                             driver.close()
                                                                             # ========[Deleting new email from inbox]===========================>
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
                                                                             # ============[finishing up logging ]================================>>
                                                                             mail_content = "Hi, Sir this is your client recharge from server 3 report from bot fo admin please check when you get time." \
                                                                                            "Thank you" \
                                                                                            "Dhritinetwork_Bot"
                                                                             sender_address = botemail
                                                                             sender_pass = botemailpassword
                                                                             receiver_address = 'ashutoshkumargautam00000@gmail.com'
                                                                             message = MIMEMultipart()
                                                                             message['From'] = sender_address
                                                                             message['To'] = receiver_address
                                                                             message[
                                                                                    'Subject'] = 'Report from Dhritinetwork_Bot for Admin'
                                                                             message.attach(
                                                                                    MIMEText(mail_content, 'plain'))
                                                                             attach_file_name = 'C:/Users/Dhritinet/PycharmProjects/Dhritinetwork_Bot/db/user_status.png'
                                                                             attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
                                                                             payload = MIMEBase('application', 'octate-stream')
                                                                             payload.set_payload((attach_file).read())
                                                                             encoders.encode_base64(payload)  # encode the attachment
                                                                             # add payload header with filename
                                                                             payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
                                                                             message.attach(payload)
                                                                             # Create SMTP session for sending the mail
                                                                             session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
                                                                             session.starttls()  # enable security
                                                                             session.login(sender_address, sender_pass)  # login with mail_id and password
                                                                             text = message.as_string()
                                                                             session.sendmail(sender_address, receiver_address, text)
                                                                             session.quit()
                                                                             logger.info("mail sent")
                                                                             #====================================================================================>>
                                                                      else:
                                                                             logger.info(" [+] Excuting main file now.. ")
                                                                             subprocess.call("python main.py")
                                                                             # =================================================================>
                                                                             # =======[The creadit Section from developer]========================>>
                                                                             logger.info(" [+] Dhritinetwork_Bot - Version 1.0")
                                                                             logger.info(" [+] Made By : Ashutosh kumar Gautam")
                                                                             logger.info(" [+] Contact me : Email - ashutoshkumargautam@protonmail.com")
                                                                             logger.info(" <-- [+] Closing Date and Time  ")
                                                                             logger.info("Back in infinite now...")
                                                                             print(" [+] Back in infinite loop now...")
                                                                             logger.info("[======================================================================================>")

                                                               subprocess.call("python main.py",shell=True)
                                   subprocess.call("python main.py", shell=True)
                     continue
