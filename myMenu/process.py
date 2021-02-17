#c'est la que la pieuvre s'execute
from emailGenerator import emailManager as EM
from emailScrapper import scraper as SCRAP
from emailThruster import reputation as REP

class Process:
    def __init__(self):
        self.pileChoice = None #on l'init a vide on attend qu'on nous le passe en argument
        # une et une seule instance
        self.emailgenerator = EM.EmailManager()  # pour module generator
        self.emailscrapper = SCRAP.Scraper()  # pour module scrapper
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
                2.5 Run
            3. EmailThruster
                3.1 Renseigner l'email
                3.2 Proxy a utiliser
                3.3 Sauvegarder les informations
            """


            if(pileChoice[0]==1):
                self.__cess1(pileChoice[1])
            if(pileChoice[0]==2):
                self.__cess2(pileChoice[1])
            if(pileChoice[0]==3):
                self.__cess3(pileChoice[1])

    def __cess1(self,choix):
        if(choix==1): #1.1 Renseigner la personne
            self.__renseigner_personne()
        if(choix==2):
            self.__generer_mails()
        if(choix==3):
            self.__sauvegarder_mails_gen()
        if(choix==4):
            self.__afficher_templates()

    def __cess2(self,choix):
        if (choix == 1):  # 1.1 Renseigner la personne
            self.__url_a_scrapp()
        if (choix == 2):
            self.__proxy_a_use_scrap()
        if (choix == 3):
            self.__set_timeout()
        if (choix == 4):
            self.__sauvegarder_mails_recup()
        if (choix == 5):
            self.__run_scrap()

    def __cess3(self,choix):
        if (choix == 1):  # 1.1 Renseigner la personne
            self.__renseigner_email()
        if (choix == 2):
            self.__proxy_a_use_thrust()
        if (choix == 3):
            self.__sauvegarder_mails_info()


    ###option menu 1
    def __renseigner_personne(self):
        nom = input("Nom ?\n")
        prenom = input("Prenom ?\n")
        self.emailgenerator.setPersonne(nom,prenom)
        print("done")

    def __generer_mails(self):
        self.emailgenerator.generateEmails()

    def __sauvegarder_mails_gen(self):
        self.emailgenerator.saveMails()
        print("done")

    def __afficher_templates(self):
        self.emailgenerator.printTemplates()


    ##option menu 2
    def __url_a_scrapp(self):
        url = input("URL ?\n ")
        self.emailscrapper.set_url(url)
        print("done")

    def __proxy_a_use_scrap(self):
        proxy = input("Proxy ? (A.A.A.A:1337) ?\n")
        self.emailscrapper.set_proxy(proxy)
        print("done")

    def __set_timeout(self):
        to = input("Timeout ? \n")
        self.emailscrapper.set_timeout(to)
        print("done")

    def __sauvegarder_mails_recup(self):
        self.emailscrapper.save_mails()
        print("done")


    def __run_scrap(self):
        self.emailscrapper.run()

    ##option menu3

    def __renseigner_email(self):
        mail = input("mail ? \n")
        if(self.emailthruster is None):
            self.emailthruster = REP.Reputation(mail)
        self.emailthruster.set_mail(mail)
        print("done")

    def __proxy_a_use_thrust(self):
        if(self.emailthruster is None):
            print("Veuillez renseigné un mail au préalable")
        else:
            proxy = input("Proxy ? (A.A.A.A:1337) ?\n")
            self.emailthruster.set_proxy(proxy)
            print("done")

    def __sauvegarder_mails_info(self):
        if (self.emailthruster is None):
            print("Veuillez renseigné un mail au préalable")
        else:
            self.emailthruster.save_response()
            print("done")

