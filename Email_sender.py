'''
Using this email sender you can send multipal message
at a time using your gmail id and password

how to use it
1)you have to create a third part app password using your gmail setting
    a)go to you gmail settings 
    b)on two step varification
    c)after that you will get an option of
    app then you have to select that and then you got a interface
    to do create the third part app
    d)there are two drop downs in first you have to choose MAIL
    e)and in the second drop down you have to choose WINDOW COMPUTER
    f)click on generate then you will get the password 

2)use this password to send the mails

NOTE: It is only for education purpas. if you misuse it then it's 
you responsibility



CREATED BY SAMRENDRA VISHWAKARMA
DATA : 24/09/2022
'''





import smtplib

#####--Enter the sender gmail address
sender_mail = input('Enter the sender Gmail: ')

#####--Enter the aap password generated by the gmail
password = input('Enter the password of sender Gmail: ')

#####--Enter the receiver gmail
receiver_mail = []

sending = int(input('How many mails do you want to send : '))
for i in range(sending):
    mail = input('Enter the receiver mail: ')
    receiver_mail.append(mail)

#####--Enter the message that you want to send
message = input('Enter the messag that you want to send: ')

##Going to the smtp server
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

### Loging into the mail sever
server.login(sender_mail,password)

### sending the message
try:
    for i in range(len(receiver_mail)):
        server.sendmail(sender_mail,receiver_mail[i],message)
        print('sending mail to', receiver_mail[i])
except:
    print('Somthing Went Wrong Please try again...')
server.quit()
print('############################ Messages send Successfully.....')

'''
CREATED BY SAMRENDRA VISHWAKARMA
DATA : 24/09/2022
'''


