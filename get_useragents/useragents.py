#!/usr/bin/python
import re
import sys
import random
import cloudscraper
from bs4 import BeautifulSoup
from get_useragents import settings

cf = cloudscraper.create_scraper(
	browser={
		"browser":"chrome", 
		"platform":"android", 
		"desktop": False
	}
)

class Get_UA:
	def __init__(self, device=None, limit=None):
		self.limit = limit
		self.max = 1001
		self.user_agents = []
		self.device = device

		if self.device and self.limit:
			if self.limit >= self.max:
				sys.exit("[!] Note the number of limits may not be more than 1000")
			else:
				if "facebook" in self.device.lower():
					self.url = settings.BASE_URL+"explore/browsers/types/application/maker/facebook-ec4"
				elif "chrome" in self.device.lower():
					self.url = settings.BASE_URL+"explore/devices/types/mobile-phone/maker/google-inc-f3d"
				elif "mozilla" in self.device.lower():
					self.url = settings.BASE_URL+"explore/devices/types/mobile-phone/maker/mozilla-foundation-757"
				elif "desktop" in self.device.lower():
					self.url = settings.BASE_URL+"explore/devices/types/desktop/maker/google-inc-f3d"
				else:
					sys.exit("[!] Error device not available at this time :(")
				self.findUserAgents()
		else:
			sys.exit("[!] Error device and string limit not detected")

	def findUserAgents(self):
		for page in range(1, 11):
			self.response = cf.get(f"{self.url}?p={page}").text
			soup = BeautifulSoup(self.response, "html.parser")
			for x in soup.find_all("td"):
				try:
					ua = re.search('\<a data-sveltekit-reload=""\ href\=\"\/(.*?)\" title="(.*?)">(.*?)<\/a>', str(x)).group(2)
					self.user_agents.append(ua)
				except:
					pass

	def GetUserAgents(self):
		while True:
			return "\n".join(self.user_agents)
			self.count +=1
			if self.count >= self.max:
				break

	def RandomUserAgents(self):
		return random.choice(self.user_agents)