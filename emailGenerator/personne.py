class Personne:
	def __init__(self, prenom=None, nom=None):

		if(prenom is None):
			prenom = "John"
		if(nom is None):
			nom = "Doe"
		self.nom = nom
		self.prenom = prenom

	def setSurname(self, nom):
		self.nom = nom

	def setFirstname(self, prenom):
		self.prenom = prenom

	def getNom(self):
		return self.nom

	def getPrenom(self):
		return self.prenom

	def toString(self):
		return self.prenom + " " + self.nom


