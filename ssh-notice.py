#!/usr/bin/env python3

import os, getpass, requests

from datetime import datetime

TOKEN = "XXXXXXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXx"
chat_id = "XXXXXXXXXXXXXXXXXXXXX"
date_time = str(datetime.today().strftime('%m-%d-%y %H:%M'))
hostname = os.uname()[1]
username = getpass.getuser()

def send_message(message):
	url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?text={message}&chat_id={chat_id}"
	requests.get(url).json()

send_message(f"SSH login attempt successful at {username}:{hostname} -  {date_time}. If you do not recognize this login, please take action ASAP.") 
