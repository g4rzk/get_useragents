#!/usr/bin/python

import re
import random
import requests
from bs4 import BeautifulSoup

class UserAgents:
	def __init__(self):
		self.url = "https://useragents.io/random?limit=1500"
		self.ua = "Mozilla/5.0 (Linux; Android 5.1; A70 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
	
	def GetUserAgent(self):
		try:
			a = requests.get(
				self.url, 
				headers={"user-agent": self.ua}, 
				timeout=1
			).text
			b = BeautifulSoup(a, "html.parser")
			for x in b.find_all("td"):
				z = re.search('\<a\ href\=\"\/(.*?)\" title="(.*?)">(.*?)<\/a>', str(x))
			
			print(z.group(2)) 
		except:
			pass