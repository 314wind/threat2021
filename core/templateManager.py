import core.template  #le notre

class TemplateManager:

	def __init__(self):
		###Liste des templates###
		self.t = []
		self.t.append(core.template.Template("$var1$var2@$domaine"))
		self.t.append(core.template.Template("$var1.$var2@$domaine"))
		print("init all templates...")
		for tmp in self.t:
			print(tmp.toString())
		print("done..... a bon entendeur")


	def addTemplate(self, string):
		self.t.append(core.template.Template(string))

	def removeTemplateFromIndice(self, indice):
		del self.t[indice]

	def removeTemplatefromTemplate(self, template):
		indice = 0
		finded = False
		#itère pour trouver le template
		for tmp in self.t:
			if (tmp.toString()==template):
				finded = True
				break
			indice+=1
		#check si trouvé on remove
		if(finded):	
			self.removeTemplateFromIndice(indice)

	def getAllTemplates(self):
		return self.t

	def toString(self):
		for tmp in self.t:
			print(tmp.toString())

#test
def sep():
	print("_________________________")

if (__name__=="__main__"):
	TM = TemplateManager()
	TM.addTemplate("$jean$dupond$@dodo$mainemaine")
	TM.toString()
	sep()
	TM.removeTemplateFromIndice(1)
	TM.toString()
	sep()
	TM.removeTemplatefromTemplate("$jean$dupond$@dodo$mainemaine")
	TM.toString()
	sep()