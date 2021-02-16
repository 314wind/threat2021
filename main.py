#for the console menu
from consolemenu import *
from consolemenu.items import *

import core.personne
import core.emailManager 


def print_banner():
	print("")
	print("\_    _____/ _____ _____ |__|  |  /   _____/ ________________  ______ ______   ___________ ")
	print("|     __)_ /      \\__  \ |  |  |  \_____  \_/ ___\_  __ \__   \ \____ \\____ \_/ __ \_  __ \ ")
	print("|         \  Y Y  \/ __ \|  |  |__/        \  \___|  | \// __ \|  |_> >  |_> >  ___/|  | \/")
	print("/_______  /__|_|  (____  /__|____/_______  /\___  >__|  (____  /   __/|   __/ \___  >__|   ")
	print("        \/      \/     \/                \/     \/           \/|__|   |__|        \/       ")

def print_menu():
	print_banner()
	print("1. EmailGenerator")
	print("2. EmailVerificator")

def get_choice():
	choice = '0'
	while(int(choice) != 1 and int(choice) != 2):
		print("enter choice between 1 and 2")
		choice = input(">")
	return choice

def main():
	print_menu()
	choice = get_choice()
	#switching the choice :
	if(choice == 1):
		pass
	if(choice == 2):
		pass
	else:
		pass

	exit()
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
	