import os
import time
import requests
import threading
from datetime import datetime
from bs4 import BeautifulSoup
from random import randint
from dotenv import load_dotenv

load_dotenv()

s = requests.session()
server_id = '808379576353947699'


class Link:
    def messages(self, api_id):
        return(f'https://discord.com/api/v8/channels/{api_id}/messages')


class Money:

    header = {'authorization':  os.getenv('DISCORD_TOKEN')}
    messages_link = Link.messages(Link, server_id)

    def send(self, content, send):
        payload = {
            'content': content,
        }
        s.post(self.messages_link, data=payload, headers=self.header)
        if send:
            print(f'sent {content} \t\t {datetime.now()}')

    def __init__(self, content, interval):

        def function_wrapper():
            while True:
                self.send(f'pls {content}', True)
                time.sleep(interval)

        t = threading.Thread(target=function_wrapper)
        t.start()

    def pm(self):
        def function_wrapper():
            responses = ['f', 'r', 'i', 'c', 'k']
            self.send(self, 'pls pm', True)
            self.send(self, responses[randint(0, len(responses)-1)], False)
            time.sleep(40)
        t = threading.Thread(target=function_wrapper)
        t.start()

    def retrieve(self):
        return (s.get(self.messages_link, headers=self.header).json())

    def dank_messages(self):
        all_ = s.get(self.messages_link, headers=self.header).json()
        dank_messages_dic = {}
        for message in all_:
            if message['author']['username'] == 'Dank Memer':
                print(message['content'].rstrip().lstrip())


Money.dank_messages(Money)
Money('beg', 50)
Money('fish', 40)
Money('hunt', 40)
Money.send(Money, 'pls dep all', False)
