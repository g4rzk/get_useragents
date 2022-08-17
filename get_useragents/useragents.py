#!/usr/bin/python
import re
import random
import requests
from bs4 import BeautifulSoup
from get_useragents import settings

class UserAgents:
	def __init__(self, limit=None):
		self.user_agents = []
		self.url = (f"https://useragents.io/random?limit={limit}")
		self.GetListUserAgents()

	def GetListUserAgents(self):
		try:
			get = requests.get(
				self.url, 
				headers={"user-agent": settings.USER_AGENT}, 
				timeout=5
			).text
			parser = BeautifulSoup(get, "html.parser")
			for x in parser.find_all("td"):
				z = re.search('\<a\ href\=\"\/(.*?)\" title="(.*?)">(.*?)<\/a>', str(x))
				self.user_agents.append(f"{z.group(2)}")
		except:
			pass

	def GetUserAgents(self):
		try:
			return "\n".join(self.user_agents)
		except IndexError:
			exit("* Error detected spam please turn on airplane mode.")

	def RandomUserAgents(self):
		try:
			return random.choice(self.user_agents)
		except IndexError:
			exit("* Error detected spam please turn on airplane mode.")