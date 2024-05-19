import smtplib
import imghdr
from email.message import EmailMessage

SENDER = "namanguptaoffical@gmail.com"
PASSWORD = "ozfk othy tupw kwqm"
RECEIVER = "namanguptabhopal@gmail.com"


def send_email(image_path):
    print("Emailing function started!")
    email_msg = EmailMessage()
    email_msg["Subject"] = "New customer just showed up!"
    email_msg.set_content("Hey we noticed a new customer!")
    # rb - read binary
    with open(image_path, "rb") as file:
        content = file.read()
    email_msg.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
    # imghdr.what()-->will find out what kind of image is this
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    # Starting servers
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_msg.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email(image_path="images/30.jpg")
