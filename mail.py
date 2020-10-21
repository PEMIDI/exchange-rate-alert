import smtplib 
from email.mime.text import MIMEText
from auth import mailtrap_username, mailtrap_password




def smtp_mail(subject, rates):

    msg = MIMEText(rates)
    msg['Subject'] = subject
    msg['From'] ='me@test.com'
    msg['To'] = 'you@test.com'

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as mailserver:
        mailserver.login(mailtrap_username, mailtrap_password)
        mailserver.sendmail(msg['From'], msg['To'], msg.as_string())

    print('email sent')


