class Personne:
	def __init__(self, prenom, nom):
		assert(nom!=prenom)
		self.nom = nom
		self.prenom = prenom

	def getNom(self):
		return self.nom

	def getPrenom(self):
		return self.prenom

	def toString(self):
		return self.prenom + " " + self.nom