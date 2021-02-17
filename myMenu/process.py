#c'est la que la pieuvre s'execute

class Process:
    def __init__(self):
        self.pileChoice = None #on l'init a vide on attend qu'on nous le passe en argument
        # une et une seule instance
        self.emailgenerator = None  # pour module generator
        self.emailscrapper = None  # pour module scrapper
        self.emailthruster = None  # pour module thruster
        #on instancie a la volet si c'est pas fait
        print("done")

    def cess(self,pileChoice):
            """
            RAPPEL STRUCTURE DES CHOIX
            1. EmailGenerator
                1.1 Renseigner la personne
                1.2 Generer des emails
                1.3 Sauvegarder les emails
                1.4 Afficher les templates
            2. EmailScrapper
                2.1 URL a scrapper
                2.2 Proxy a utiliser
                2.3 Set le timeout
                2.4 Sauvegarder les emails récupérés
            3. EmailThruster
                3.1 Renseigner l'email
                3.2 Proxy a utiliser
                3.3 Sauvegarder les informations
            """
            print("HEREHRHEE")
            if(pileChoice[0]==1):
                self.__cess1(pileChoice[1])
            if(pileChoice[0]==2):
                self.__cess2(pileChoice[1])
            if(pileChoice[0]==2):
                self.__cess3(pileChoice[1])

    def __cess1(self,choix):
        if(choix==1): #1.1 Renseigner la personne

            pass
    def __cess2(self,choix):
        print("Processing myMenu 1 and choice :", choix)
        pass

    def __cess3(self,choix):
        print("Processing myMenu 1 and choice :", choix)
        pass

