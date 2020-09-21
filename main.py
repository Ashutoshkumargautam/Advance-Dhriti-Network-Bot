#!/usr/bin/env python3
import datetime
from time import sleep
from selenium import webdriver
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import imaplib, email
import logging
import os
#===[Dhritinetwork_BOT_DATA_CENTER]=============================================>>
#===[All server information here]==========>>
#=====[server1]==============================>
s1_admin_username = "Anil"
s1_admin_password = "Anil2522"
#=====[server2]===============================>
s2_admin_username = "_"
s2_admin_password = "_"
#=====[server3]===============================>
s3_admin_username = "operator"
s3_admin_password = "Anil@2515"
#============================================>>
#=======[Bot using email and password]================>
botemail = "xyzxxxaxbxzx123@gmail.com"
botemailpassword = "xxx@123456"
#========[Admin email here]==========================>
adminEmail = "ashutoshkumargautam00000@gmail.com"
#=========================================================================================>>
while True:
       #Reading email here........
       # Create and configure logger
       logging.basicConfig(filename="Dhritinetwork_Bot.log",
                           format='%(asctime)s %(message)s',
                           filemode='w')
       # Creating an object
       logger = logging.getLogger()
       # Setting the threshold of logger to DEBUG
       logger.setLevel(logging.DEBUG)
       #---------------------------->
       logger.info(" [+] Reading Email sent by website. ")
       #Reading email here.
       #=================================>
       user = botemail
       password = botemailpassword
       imap_url = 'imap.gmail.com'
       # Function to get email content part i.e its body part
       def get_body(msg):
              if msg.is_multipart():
                     return get_body(msg.get_payload(0))
              else:
                     return msg.get_payload(None, True)
       # Function to search for a key value pair
       def search(key, value, con):
              result, data = con.search(None, key, '"{}"'.format(value))
              return data
       # Function to get the list of emails under this label
       def get_emails(result_bytes):
              msgs = []  # all the email data are pushed inside an array
              for num in result_bytes[0].split():
                     typ, data = con.fetch(num, '(RFC822)')
                     msgs.append(data)
              return msgs
       # this is done to make SSL connnection with GMAIL
       con = imaplib.IMAP4_SSL(imap_url)
       # logging the user in
       con.login(user, password)
       # calling function to check for email under this label
       con.select('Inbox')
       # fetching emails from this user "tu**h*****1@gmail.com"
       msgs = get_emails(search('FROM', adminEmail, con))
       # Uncomment this to see what actually comes as data
       # print(msgs)
       # Finding the required content from our msgs
       # User can make custom changes in this part to
       # fetch the required content he / she needs
       # printing them by the order they are displayed in your gmail
       for msg in msgs[::-1]:
              for sent in msg:
                     if type(sent) is tuple:
                            # encoding set as utf-8
                            content = str(sent[1], 'utf-8')
                            data = str(content)
                            # Handling errors related to unicodenecode
                            try:
                                   indexstart = data.find("ltr")
                                   data2 = data[indexstart + 5: len(data)]
                                   indexend = data2.find("</div>")
                                   # printtng the required content which we need
                                   # to extract from our email i.e our body
                                   y = data2[0: indexend]
                                   #writing email into the mail_data_file.txt
                                   f = open("mail_data_file.txt", "w")
                                   f.write(y)
                                   f.close()
                            except UnicodeEncodeError as e:
                                   pass
                     # now searching what is name of the user who to recharge...
              for LINE in open("test.txt"):
                     STRING = "Name:"
                     if STRING in LINE:
                            username = LINE
              nameofuser = username
              print(nameofuser)
       print(' [+] Waitting for website info  and payment of coustumer > ')
       x = input()
       print(" [+] Successfully connected Now ," + x)
       logger.info(" [+] Colleting user information from email... ")
       logger.info(" [+] Louching browser now....")
       logger.info(" <-- [+] Staring Date and Time ")
       driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")
       driver.get('https://partner.gtel.in/Partner/Default.aspx')
       sleep(1)
       #============[Bot is click and input the username here]================
       driver.find_element_by_xpath('//*[@id="txtUserName"]').click()
       driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(s1_admin_username)
       #============[Bot is click and input the Password here]================
       driver.find_element_by_xpath('//*[@id="txtPassword"]').click()
       driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(s1_admin_password)
       #============[Bot is now clicking on login button to login in the website]====
       driver.find_element_by_xpath('//*[@id="save"]').click()
       #=======[ Now bot is trying to all user account ]=====================
       driver.get('https://partner.gtel.in/Partner/Accounts.aspx')
       sleep(1)
       #======[ Now bot is trying to click search bar   ]=========================
       driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtserch"]').click()
       #======[ Now bot is trying type on search bar  ]==============================================>>
       driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtserch"]').send_keys(nameofuser)
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
       attachment = open("C:/Users/Perfect TC Society/PycharmProjects/Dhritinetwork_Bot/" + filename, "rb")
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
       logger.info(" [+] Deleting New screenshot for managing space for another.")
       #====[Now sending email to the clients]===============================>
       # me == my email address
       # you == recipient's email address
       me = botemail
       you = "nameofuser"
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
       logger.info(" [+] Successfully Email sent to coustumer")
       #===========[All Task Complete successfully logout now..]=======>>
       driver.find_element_by_xpath('//*[@id="lbklogout"]').click()
       sleep(2)
       logger.info(" [+] Successfully task completed Now.")
       logger.info(" [+] Closing entire browser")
       """ Here Bot is trying close entire browser """
       driver.close()
       #====[Deleting unwanted things area]==========================>>>
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
       #===========[Now deleting screenshot for managing space to next screenshot]=======>>
       os.remove("user_status.png")
       #============[finishing up logging ]================================>>
       #The creadit Section from developer
       logger.info(" [+] Dhritinetwork_Bot - Version 1.0")
       logger.info(" [+] Made By : Ashutosh kumar Gautam")
       logger.info(" [+] Contact me : Email - ashutoshkumargautam@protonmail.com")
       logger.info(" <-- [+] Closing Date and Time  ")
       logger.info("[======================================================================================>")
