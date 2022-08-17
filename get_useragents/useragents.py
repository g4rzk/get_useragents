#!/usr/bin/python

import re
import random
import requests
from bs4 import BeautifulSoup

class UserAgents:
	def __init__(self, limit=None):
		self.user_agents = []
		self.url = f"https://useragents.io/random?limit={limit}"
		self.ua = "Mozilla/5.0 (Linux; Android 5.1; A70 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
		self.GetListUserAgents()

	def GetListUserAgents(self):
		try:
			get = requests.get(
				self.url, 
				headers={"user-agent": self.ua}, 
				timeout=1
			).text
			parser = BeautifulSoup(get, "html.parser")
			for x in parser.find_all("td"):
				z = re.search('\<a\ href\=\"\/(.*?)\" title="(.*?)">(.*?)<\/a>', str(x))
				self.user_agents.append(f"{z.group(2)}\n")

		except:
			pass

	def GetUserAgents(self):
		return "".join(self.user_agents)

	def RandomUserAgents(self):
		return random.choice(self.user_agents)