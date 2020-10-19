import smtplib 






def smtp_mail(rates, receiver, subject):
    
    sender = 'me@test.com'

    message = f"""\
    subject : {subject}
    To: {receiver}
    From: {sender}
    {rates}."""

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as mailserver:
        mailserver.login("a938bb33b3f298", "ed8794b056db1a")
        mailserver.sendmail(sender, receiver, message)

    print('email sent')