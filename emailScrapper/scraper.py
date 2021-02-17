#Scrape email addresses given a specific URL

#Proxy list -> https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt

import re
import requests
import random

class Scraper:
	def __init__(self, url=None, proxy="no"):
		self.regex = r'(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?!(png|jpg|jpeg)$)*[A-Za-z]{2,6}\b)'
		self.url = url
		self.response_html_text = ""
		self.emails = []
		self.timeout = 20
		self.proxies = {}

		if(proxy == "yes"):
			self.choose_proxy()

	def set_url(self,url):
		self.url = url

	def set_timeout(self, to):
		self.timeout = to

	def load_proxies(self):
		#print("loading proxies")
		proxies = list()
		with open("../res/proxy_list.txt", "r") as f:
			lignes = f.readlines()
			for ligne in lignes:
				#print(ligne.strip())
				proxies.append(ligne.strip())
		return proxies

	def choose_proxy(self):
		proxy = random.choice(self.load_proxies())
		#print(proxy)
		#51.255.48.61:9999 is working for tests
		self.proxies = {
			"http": "51.255.48.61:9999", #Then change to proxy
			"https": "51.255.48.61:9999",
		}
		#print(self.proxies)

	def set_proxy(self, proxy):
		self.proxies = {
			"http": proxy,
			"https" : proxy
		}

	def request(self):
		try:
			if(self.url is None):
				print("Veuillez renseigner un url a scrapper")
			else:#url is not none
				if(requests.get(url=self.url, proxies=self.proxies, timeout=self.timeout).status_code == 200):

					#Check if we can access the website (return code)
					self.response_html_text = requests.get(url=self.url, proxies=self.proxies, timeout=self.timeout).text
				else:
					print("Can't access URL")
					return
		except requests.exceptions.ProxyError:
			print("Can't connect through proxy")
			#Restart only if option --retry ?
			#self.choose_proxy()
			#self.request()

		except requests.exceptions.Timeout:
			print("Timeout reached")
			#Restart only if option --retry ?
			#self.choose_proxy()
			#self.request()


	def parse_results(self):
		if(self.response_html_text != ""):
			#Set to remove duplicates
			matches = re.findall(self.regex, self.response_html_text)

			for emails in matches:
				for email in emails:
					if(email != ''):
						self.emails.append(email)
		else:
			print("Can't parse results")
			return

	def get_mails(self):
		if(len(self.emails) != 0):
			for mail in self.emails:
				print(mail)
		else:
			print("No emails found")
			return

	def save_mails(self):
		with open("res/mail_scrapped.dat", "w") as f:
			f.write(self.emails)

	def run(self):
		self.request()
		self.parse_results()
		self.get_mails()



if(__name__ == "__main__"):
	scraper = Scraper("https://fitsmallbusiness.com/professional-email-address-ideas/", proxy="yes")
	scraper.run()
	#scraper.load_proxies()
