#!/usr/bin/python
import re
import random
import cloudscraper
from bs4 import BeautifulSoup
from get_useragents import settings

UA = random.choice(
	settings.USERAGENTS
)
cf = cloudscraper.create_scraper(
	browser={
		"browser":"chrome", 
		"platform":"android", 
		"desktop": False
	}
)

class UserAgents:
	def __init__(self, limit=None):
		self.user_agents = []
		self.url = (f"https://useragents.io/random?limit={limit}")
		self.GetListUserAgents()

	def GetListUserAgents(self):
		try:
			get = cf.get(
				self.url
			).text
			parser = BeautifulSoup(get, "html.parser")
			for x in parser.find_all("td"):
				z = re.search('\<a\ href\=\"\/(.*?)\" title="(.*?)">(.*?)<\/a>', str(x))
				self.user_agents.append(f"{z.group(2)}")
		except:
			pass

	def GetUserAgents(self):
		return "\n".join(self.user_agents)

	def RandomUserAgents(self):
		return random.choice(self.user_agents)