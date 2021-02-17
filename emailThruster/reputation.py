import requests
import json
import random

class Reputation:
	def __init__(self, mail, proxy="no"):
		self.mail = mail
		self.url = "https://emailrep.io/" + mail
		self.response_html_text = ""
		self.timeout = 20
		self.proxies = {}

		if(proxy == "yes"):
			self.choose_proxy()


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
		print(proxy)
		#51.255.48.61:9999 is working for tests
		self.proxies = {
			"http": "106.14.248.171:8080", #Then change to proxy
			"https": "106.14.248.171:8080",
		}
		#print(self.proxies)


	def request(self):
		try:
			if(requests.get(url=self.url, proxies=self.proxies, timeout=self.timeout).status_code == 200):

				#Check if we can access the website (return code)
				self.response_html_text = requests.get(url=self.url, proxies=self.proxies, timeout=self.timeout).text
			else:
				print("Can't access URL")
				return
		except requests.exceptions.ProxyError:
			print("Can't connect through proxy")
			#Restart only if option --retry ?
			self.choose_proxy()
			self.request()

		except requests.exceptions.Timeout:
			print("Timeout reached")
			#Restart only if option --retry ?
			self.choose_proxy()
			self.request()
#{'email': 'gouthp@gmail.com', 'reputation': 'high', 'suspicious': False, 'references': 6, 'details': {'blacklisted': False, 
#'malicious_activity': False, 'malicious_activity_recent': False, 'credentials_leaked': True, 'credentials_leaked_recent': False, 
#'data_breach': True, 'first_seen': '02/28/2013', 'last_seen': '01/13/2020', 'domain_exists': True, 'domain_reputation': 'n/a', 
#'new_domain': False, 'days_since_domain_creation': None, 'suspicious_tld': False, 'spam': False, 'free_provider': True, 
#'disposable': False, 'deliverable': True, 'accept_all': False, 'valid_mx': True, 'primary_mx': 'gmail-smtp-in.l.google.com', 
#'spoofable': True, 'spf_strict': True, 'dmarc_enforced': False, 'profiles': ['twitter']}}

	def parse_results(self):
		if(self.response_html_text != ""):
			json_array = json.loads(self.response_html_text)
			print("Email searched : " + json_array['email'])
			print("Reputation level : " + json_array['reputation'])
			print("Suspicious : " + str(json_array['suspicious']))
			print("Blacklisted email : " + str(json_array["details"]['blacklisted']))
			#If True then search on HaveIBeenPwned
			print("Credentials leaked : " + str(json_array["details"]['credentials_leaked']))
			print("Spam email address : " + str(json_array["details"]['spam']))
			print("Spoofable email address : " + str(json_array["details"]['spoofable']))
			if(len(json_array["details"]['profiles']) != 0):
				print("Email found on : ")
				for service in json_array["details"]['profiles']:
					print("- " + service)
		else:
			print("Can't parse results")
			return


	def run(self):
		self.request()
		self.parse_results()



if(__name__ == "__main__"):
	reputation = Reputation("zworkrowz@gmail.com", proxy="yes")
	reputation.run()
	#scraper.load_proxies()