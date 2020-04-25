import smtplib
import readfromfile
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

f = open('./loginMail.txt','r')
logins = f.readlines()
login_mails = []
for j in logins:
    login_mails.append(j.strip())
# print(login_mails)
subject = str(input("please input subject : "))
txt  = str(input("please input body : "))
count = int(input("please input number of mail : "))
to_mails,bcc_mails = readfromfile.send_email(count)
okmails = open('./successLog.txt','w')
blockmails = open('./failedLog.txt', 'w')
for i in login_mails:
    try :
        print(i)
        msg = MIMEMultipart()
        msg['From'] = i
        msg['To'] = to_mails[login_mails.index(i)]
        msg['Bcc'] = ", ".join(bcc_mails[login_mails.index(i)])
        msg['Subject'] = subject
        msg.attach(MIMEText(txt))
        text = msg.as_string()
        # print("___________",text)
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(i, "nJVx2@unLvK8AgjQ")
        # server.sendmail(i,to_mails[login_mails.index(i)], msg.as_string())
        server.quit()
        okmails = open('./successLog.txt','a')

        okmails.write("login with : " + i + "\n"
                      + "To : " + msg['To'] + "\n"
                      + "Bcc : " +  msg['Bcc'] + "\n"
                      + "subject : "  + subject + "\n"
                      + "text: " + txt + "\n"
                      + "--------------------------"+ "\n")
        okmails.close()
        print("success")
    except:
        msg = MIMEMultipart()
        msg['To'] = to_mails[login_mails.index(i)]
        msg['Bcc'] = ", ".join(bcc_mails[login_mails.index(i)])
        print("_______________ERR__________________")
        blockmails = open('./failedLog.txt', 'a')
        blockmails.write("login with : " + i + "\n"
                      + "To : " + msg['To'] + "\n"
                      + "Bcc : " + msg['Bcc'] + "\n"
                      + "subject : " + subject + "\n"
                      + "text: " + txt + "\n"
                      + "--------------------------"+ "\n")
        blockmails.close()
        print("_____________________________________")

#
# f  = open('./mail-send-list.txt')
# mailList = []
# for i in f.readlines() :
#     # mailList.append(i.strip())
#     print(i.strip())
#     try:
#         email_user = i.strip()
#         email_password = 'nJVx2@unLvK8AgjQ'
#         # email_password = 'hamed856658@!hamed'
#         server = smtplib.SMTP('smtp.office365.com',587)
#         server.starttls()
#         server.login(email_user,email_password)
#         server.quit()
#         print("Log in : ", i.strip())
#     except:
#         print("Log in ERR : ",i.strip())
#         r = open('./blockedMails.txt','a')
#         r.write(i.strip() + '\n')
#         r.close()
