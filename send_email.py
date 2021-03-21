# import requests
import smtplib


class SendEmail:
    def __init__(self, main_subject, main_body, main_recipient):
        self.subject = main_subject
        self.body = main_body
        self.recipient = main_recipient
        self.sender_email = 'typeYourEmail@domain.com'
        self.password = 'typeYourPassword'

    def send_mail(self):
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        conn.starttls()
        conn.login(self.sender_email, self.password)
        print("Login success")
        return conn


    def main(self):
        try:
            server = self.sender_email()
            server.sendmail(self.sender_email, self.recipient, self.body)
            print('Email sent!')
        except Exception as e:
            print('Email not sent!')


if __name__ == '__main__':
    subject = raw_input("Subject? ")
    body = raw_input("Body? ")
    recipient = raw_input("Recipient? ")
    mail = SendEmail(subject,body,recipient)
    mail.main()