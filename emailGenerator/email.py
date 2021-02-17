class Email:
	def __init__(self, email):
		self.email = email

	def getMail(self):
		return self.email

	def setMail(self, email):
		self.email = email

	def toString(self):
		return self.email