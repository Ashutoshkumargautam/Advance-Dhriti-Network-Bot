#!/usr/bin/env python3
from time import sleep
from selenium import webdriver
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import imaplib
import smtplib
import logging
import re
import shutil
import email
import sys
import time
import parser
import os
#============================>>>
s1_admin_username = "Anil"
s1_admin_password = "Anil2522"
botemail = "xyzxxxaxbxzx123@gmail.com"
botemailpassword = "xxx@123456"
#========[Admin email here]==========================>
adminEmail = "ashutoshkumargautam00000@gmail.com"
#==============================================================>>
#=====[Making log file here]================>
logging.basicConfig(filename="Dhritinetwork_Bot.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#=====================================================>
#===================================[program logic]============================================>>
""" When new email comes then bot will capture that email and doing work it own way
if any email is not coming so that time bot will waitting for intire time."""
#================================================================================================>>
#=============[Reading email here..]===============================>>
imap_url = 'imap.gmail.com'
# ---------------------------------->
mail = imaplib.IMAP4_SSL(imap_url)
mail.login(botemail, botemailpassword)
# ---------------------------------->
num_of_mail = 0
# ---------------------------------->
while True:
       #=======[Loader start here]=========>>
       #=======================================================================================>>>
       # 2nd -> if any email is not comming in bot email box then wait  infinite time....
       print("Waitting for website response...")
       # ---------------------------------->
       # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
       animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                    "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
       for i in range(len(animation)):
              time.sleep(0.2)
              sys.stdout.write("\r" + animation[i % len(animation)])
              sys.stdout.flush()
       print("\n")
       #======[loader end]=================================================>>
       mail.select('inbox')

       type, data = mail.search(None, '(UNSEEN)')
       mail_ids = data[0]
       id_list = mail_ids.split()

       if len(id_list) > num_of_mail:
              # ================================================================================>>
              # 1st -> if any new email came in bot email box then read that email and cature all information inside email...
              f = open("test_1.txt", "w")
              f.write("true")
              f.close()
              f = open("test_1.txt", "r")
              website_response = f.read()
              #=============================================================>>
              for i in reversed(id_list):
                     type, data = mail.fetch(i, '(RFC822)')
              #==============================================================>>
                     for response_part in data:
                         if isinstance(response_part, tuple):
                             msg = email.message_from_string(response_part[1].decode('utf-8', errors='ignore'))
                             email_subject = msg['subject']
                             email_from = msg['from']

              num_of_mail = len(id_list)
              if website_response == 'true':
                     print("okay i am doing work now..")
              break
       continue
       #=======[if any new email is not comming so back from here.]=========>>
       #===================================================================>>>
       print(" [+] Successfully connected Now ")
       logger.info(" [+] Colleting user information from email... ")
       logger.info(" [+] Louching browser now....")
       logger.info(" <-- [+] Staring Date and Time ")
       #==================================================================================>>>
       driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")
       driver.get('https://partner.gtel.in/Partner/Default.aspx')
       sleep(1)
       #============[Bot is click and input the username here]================>>>
       driver.find_element_by_xpath('//*[@id="txtUserName"]').click()
       driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(s1_admin_username)
       #============[Bot is click and input the Password here]================>>>
       driver.find_element_by_xpath('//*[@id="txtPassword"]').click()
       driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(s1_admin_password)
       #============[Bot is now clicking on login button to login in the website]====>>>
       driver.find_element_by_xpath('//*[@id="save"]').click()
       #=======[ Now bot is trying to all user account ]=====================>>>
       driver.get('https://partner.gtel.in/Partner/Accounts.aspx')
       sleep(1)
       #======[ Now bot is trying to click search bar   ]===============================>>>
       driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtserch"]').click()
       #======[ Now bot is trying type on search bar  ]==============================================>>
       driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtserch"]').send_keys(username)
       sleep(1)
       #======[click on search button]===========================================
       driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnserch"]').click()
       sleep(1)
       #================[Bot is trying to click on renew plan]=======================================>>>
       popup = driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/div[1]/div[1]/table/tbody/tr/td[2]/div[1]/div/div/table/tbody/tr[2]/td[12]/input').click()
       sleep(2)
       #==============[Scroll here this gonna be easy]=========================================>>>
       scr1 = driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/div[1]/div[3]')
       driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
       sleep(2)
       #--[Bot is clicking on cancel button on popup-->>
       driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/div[1]/div[3]/table/tbody/tr[40]/td/button[2]').click()
       sleep(2)
       #============[This is reporting section start here]===============================>>>
       driver.save_screenshot("user_status.png")
       logger.info(" [+] Screenshot taken successfully")
       # ===========[Now moving to another folder screenshot for managing space to next screenshot]=======>>
       original = r'C:/Users/Perfect TC Society/PycharmProjects/Dhritinetwork_Bot/user_status.png'
       target = r'C:/Users/Perfect TC Society/PycharmProjects/Dhritinetwork_Bot/db/user_status.png'
       shutil.move(original, target)
       #===========[sending email to admin]=======>>
       #==[sender email here ]=========================>>>
       fromaddr = botemail
       #==[Recevier email here ]=========================>>>
       toaddr = adminEmail
       # instance of MIMEMultipart
       msg = MIMEMultipart()
       # storing the senders email address
       msg['From'] = fromaddr
       # storing the receivers email address
       msg['To'] = toaddr
       # storing the subject
       msg['Subject'] = "From_Server_Dhritinetworkbot_Repoert"
       # string to store the body of the mail
       body = "Hello Sir, This is your report from Server_Bot which is handle your all wifi network user" \
              "please sir, check this screenshot with attach with email i have complete a user renewal 1min. ago." \
              "Thank you"
       # attach the body with the msg instance
       msg.attach(MIMEText(body, 'plain'))
       # open the file to be sent
       filename = "user_status.png"
       attachment = open("C:/Users/Perfect TC Society/PycharmProjects/Dhritinetwork_Bot/db/" + filename, "rb")
       # instance of MIMEBase and named as p
       p = MIMEBase('application', 'octet-stream')
       # To change the payload into encoded form
       p.set_payload(attachment.read())
       # encode into base64
       encoders.encode_base64(p)
       p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
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
       logger.info(" [+] Successfully Email sent to Admin")
       #====[Now sending email to the clients]===============================>
       logger.info(" [+] Successfully Email sent to coustumer")
       #===========[All Task Complete successfully logout now..]=======>>
       driver.find_element_by_xpath('//*[@id="lbklogout"]').click()
       sleep(2)
       logger.info(" [+] Successfully task completed Now.")
       logger.info(" [+] Closing entire browser")
       """ Here Bot is trying close entire browser """
       driver.close()
       #============[Sending email to the client]========================>>
       searchfile = open("mail_data_file.txt", "r")
       for line in searchfile:
              if "Email:" in line:
                     f = open('email.txt', 'w')
                     f.write(line)
       searchfile.close()
       f = open('email.txt', 'r')
       useremail = f.read()
       # ===============================================================>>
       me = botemail
       you = useremail
       # Create message container - the correct MIME type is multipart/alternative.
       msg = MIMEMultipart('alternative')
       msg['Subject'] = "Dhritinetwork congratulation"
       msg['From'] = me
       msg['To'] = you
       # Create the body of the message (a plain-text and an HTML version).
       text = "\n\n\n"
       html = """\
       <html>
         <head></head>
         <body style="background-color:powderblue;">
         <center>
         <h1 style="color:green;">Dhriti Consultancy and Services - Dhriti Network </h1>
           <h2>Hi!<br>
              <h2>Ashutosh kumar gautam</h2>
              <h1 style="color:red;">Congratulation your internet recharge successfully Done.</h1>
           </h2>
           </center>
         </body>
       </html>
       """
       # Record the MIME types of both parts - text/plain and text/html.
       part1 = MIMEText(text, 'plain')
       part2 = MIMEText(html, 'html')
       # Attach parts into message container.
       # According to RFC 2046, the last part of a multipart message, in this case
       # the HTML message, is best and preferred.
       msg.attach(part1)
       msg.attach(part2)
       # Send the message via local SMTP server.
       mail = smtplib.SMTP('smtp.gmail.com', 587)
       mail.ehlo()
       mail.starttls()
       mail.login(botemail, botemailpassword)
       mail.sendmail(me, you, msg.as_string())
       mail.quit()
       # ========================================>>
       #===[Deleting email]=================================================>>>
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
       logger.info("[======================================================================================>")
       print("Back in infinite loop now...  ")
       continue
