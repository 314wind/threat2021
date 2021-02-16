import core.template  #le notre

class TemplateManager:

	def __init__(self,filename=None):
		###Liste des templates###
		self.t = []
		
		if(filename is not None):#un nom de fichier a ete renseigne pour lire les templates
			print("init templates from files...")
			self.__fileLoad(filename) #init nos templates par fichiers
			print("done.....")
		else:
			self.__defaultLoad() #init nos deux templates
			print("done.....")
		

	def __fileLoad(self,filename):
		try:
			with open(filename, "r") as f: #ouverture du fichier
				lines = f.readlines()
				for line in lines:#parcours de chaque ligne
					if(line.count('@')!=1):#on verifie que y'a qu'un seul @ dans le template 
						print(">>template : ", line,"as to many @")
						continue
					self.t.append(core.template.Template(line))
				for tmp in self.t: #DEBUG
					print(tmp.toString())
		except IOError:
			print("error while opening file, loading default templates")
			self.__defaultLoad()

	def __defaultLoad(self):
		print ("file not found loading default template")
		self.t.append(core.template.Template("$var1$var2@$domaine"))
		self.t.append(core.template.Template("$var1.$var2@$domaine"))
		for tmp in self.t: #DEBUG
			print(tmp.toString())


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