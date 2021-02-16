#for socialsccan
from socialscan.util import Platforms, sync_execute_queries

import core.personne
import core.emailManager 


def main():

	EM = core.emailManager.EmailManager()
	Quentin = core.personne.Personne("Pierre", "Gouth")
	EM.generateEmails(Quentin)
	#EM.toString()
	mails = EM.getMailsAsString() # ici on a la liste des mails généré 


"""
	queries = ["gouthp@gmail.com"]#mails
	platforms = [Platforms.GITHUB]
	proxy_list = []
	with open("proxy_list.txt", "r") as f:
		lignes = f.readlines()
		for ligne in lignes:
			proxy_list.append(ligne.strip())
	results = sync_execute_queries(queries, platforms)#,proxy_list)
	for result in results:
	    print(f"{result.query} on {result.platform}: {result.message} (Success: {result.success}, Valid: {result.valid}, Available: {result.available})")
"""
"""
	for email in mails:
	#email = mails[0]
		out = []
		client = httpx.AsyncClient()

		await discord(email, client, out)

		print(email.toString(),":",out)
		await client.aclose()
 """   


if(__name__=="__main__"):
	main()
	