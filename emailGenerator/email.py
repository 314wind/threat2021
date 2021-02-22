import re

class Email:
	def __init__(self, email):
		#Verify the email when it's initialized
		self.setMail(email)

	def getMail(self):
		return self.email

	def setMail(self, email):
		if(self.verifyMail(email)):
			self.email = email
		else:
			print("Mail not valid")
			self.email = None

	def verifyMail(self, email):
		regex = "^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$"
		##Verify regex and length of left part
		return re.match(regex, email.strip()) and len(email.split("@")[0]) >= 2

	def toString(self):
		return self.email


if(__name__ == "__main__"):
	mail = Email("zworkrowz@gmail.com")
	print(mail.getMail())
	mail.setMail("test\\.test@gmail.com")
	print(mail.getMail())
	mail.setMail("aa@gmail.com")
	print(mail.getMail())
	print(type(mail))