import emailGenerator.templateManager as TM
import emailGenerator.personne
import emailGenerator.email

import re

class EmailManager:
	def __init__(self):
		self.tm = TM.TemplateManager("res/templates.dat") #template manager
		self.listMails = []
		self.DOMAINES = []
		with open("res/domaines.txt", "r") as f:
			lignes = f.readlines()
			for ligne in lignes:
				self.DOMAINES.append(ligne.strip())

		self.DATES = [i for i in range(1950,2010)]
		self.NOMBRES = [i for i in range(0,99)]

		self.NOMBRES_RANDOM = -1
		self.personne = None


	def setPersonne(self, nom, prenom):
		self.personne = emailGenerator.personne.Personne(prenom, nom)

	def getMails(self):
		return self.listMails

	def getMailsAsString(self):
		res = []
		for mails in self.listMails:
			res.append(mails.toString())
		return res 
		
	def toString(self):
		for mail in self.listMails:
			print(mail.toString())

	def addEmails(self, emails):
		for e in emails:
			self.listMails.append(emailGenerator.email.Email(e))


	def saveMails(self):
		with open("res/mails_saved.dat", "w+") as f:
			for mail in self.listMails:
				f.write(mail.toString()+"\n")
		print("Done saving")

	def printTemplates(self):
		self.tm.toString()

	###TODO
	#		get un email dans la liste
	#		get un email par rapport a son indice

	def generateEmails(self):
		liste_templates = self.tm.getAllTemplates()
		if(self.personne is None):
			print("Il faut renseigner d'abord une personne")
			return

		nom = self.personne.getNom()
		prenom = self.personne.getPrenom()
		#on bind les paramètres
		#parcours templates
		for tmp in liste_templates: #on itère sur des objets string.Template
			emails = self.fillTemplate(tmp,nom,prenom)
			checked_emails = self.checkEmails(emails)
			self.addEmails(checked_emails)
		self.toString()
		print("\n\n")


	def fillTemplate(self, template, var1, var2): #template, nom, prenom
		args = 	[ var1, var2, var1[0], var2[0],
				  var1.upper(), var2.upper(),
				  var1.lower(), var2.lower(),
				  var1[0].upper(), var2[0].upper(),
				  var1[0].lower(), var2[0].lower()]

		emails = []
		for domaine in self.DOMAINES:
			for i in range (0,len(args)):
				for j in range(0, len(args)):
					if(i!=j):
						emails.append(template.getTemplate().substitute(var1=args[i], var2=args[j], domaine=domaine))
		return emails

	def checkEmails(self, emails):
		res = []
		regex = "^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$"

		for email in emails:
			#If email is valid
			if(re.match(regex,email.strip())):
				lpart,rpart = email.split("@")
				if(len(lpart)>=4):
					res.append(email.strip())
		return res

def sep():
	print("_________________________")

if (__name__=="__main__"):
	EM = EmailManager()
	EM.setPersonne("SIMIER", "Quentin")
	EM.generateEmails()
	EM.toString()

	