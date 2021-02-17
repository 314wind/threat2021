"""
exemple :
from string import Template
t = Template($nom.$prenom@$domaine)
t.substitute(nom=var1, prenom=var2, domaine=var3)
"""
from string import Template as Modele

class Template:
	def __init__(self,string):
		self.t = Modele(string)

	def getTemplate(self):
		return self.t

	def setTemplate(self, string):
		self.t = Modele(string)

	def toString(self):
		return self.t.template