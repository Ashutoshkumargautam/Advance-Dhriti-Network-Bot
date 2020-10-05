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
#===[All server information here]==========>>
#=====[server1]==============================>
s1_admin_username = "Anil"
s1_admin_password = "Anil2522"
#=======[Bot using email and password]================>
botemail = "xyzxxxaxbxzx123@gmail.com"
botemailpassword = "xxx@123456"
#========[Admin email here]==========================>
adminEmail = "ashutoshkumargautam00000@gmail.com"
emailofuser = "ashutoshkumargautam@protonmail.com"
#==============================================================>>
while True:
       print(" [+] Reading Email...")
       #=====[Making log file here]================>
       logging.basicConfig(filename="Dhritinetwork_Bot.log",
                           format='%(asctime)s %(message)s',
                           filemode='w')
       logger = logging.getLogger()
       logger.setLevel(logging.DEBUG)
       #=====================================================>
       logger.info(" [+] Reading Email sent by website. ")
       #=====================================================>
       #======[Reading emails here...]=====================>>
       user = botemail
       password = botemailpassword
       imap_url = 'imap.gmail.com'
       def get_body(msg):
              if msg.is_multipart():
                     return get_body(msg.get_payload(0))
              else:
                     return msg.get_payload(None, True)
       # Function to search for a key value pair
       def search(key, value, con):
              result, data = con.search(None, key, '"{}"'.format(value))
              return data
       def get_emails(result_bytes):
              msgs = []
              for num in result_bytes[0].split():
                     typ, data = con.fetch(num, '(RFC822)')
                     msgs.append(data)
              return msgs
       con = imaplib.IMAP4_SSL(imap_url)
       con.login(user, password)
       con.select('Inbox')
       msgs = get_emails(search('FROM', 'test@hostinger-tutorials.com', con))
       for msg in msgs[::-1]:
              for sent in msg:
                     if type(sent) is tuple:
                            content = str(sent[1], 'utf-8')
                            data = str(content)
                            try:
                                   indexstart = data.find("ltr")
                                   data2 = data[indexstart + 5: len(data)]
                                   indexend = data2.find("</div>")
                                   y = data2[0: indexend]
                                   # writing email into the mail_data_file.txt
                                   # --------------------------------------------->
                                   f = open("mail_data_file.txt", "w")
                                   f.write(y)
                                   f.close()
                                   # done
                                   # ===============================================>>
                                   # reading email here...
                                   with open('mail_data_file.txt', 'r') as file:
                                          for line in file:
                                                 for word in line.split():
                                                        # reading the file writting splited word inside the text file.
                                                        f = open("test.txt", "w")
                                                        # ignoring the html here....
                                                        v = word
                                                        result = re.sub("<.*?>", "", v)
                                                        clean = result
                                   f.write(clean)
                                   f.close()
                                   # reading again text1 file then printing the file on the screen.
                                   f = open("test.txt", "r")
                                   nameofuser = f.read()
                                   username = nameofuser
                                   print(username)
                                   #==========================================>>
                            except UnicodeEncodeError as e:
                                   pass
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
       #=================================================================>>>
       #============[Sending email to the client]========================>>
       #===============================================================>>
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
