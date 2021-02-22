#c'est la que la pieuvre s'execute
from emailGenerator import emailManager as EM
from emailScrapper import scraper as SCRAP
from emailThruster import reputation as REP

class Connector:
    __instance = None
    @staticmethod
    def getInstance():
        #leasy instance
        if Connector.__instance == None:
            Connector()
        return Connector.__instance

    def __init__(self):
        if(Connector.__instance == None):
            Connector.__instance = self

        self.pileChoice = None #on l'init a vide on attend qu'on nous le passe en argument
        # une et une seule instance
        self.emailgenerator = EM.EmailManager()  # pour module generator
        self.emailscrapper = SCRAP.Scraper()  # pour module scrapper
        self.emailthruster = None  # pour module thruster
        #on instancie a la volet si c'est pas fait
        print("done")


    ###option menu 1
    def configure_firstname(self):
        prenom = input("Firstname ?\n")
        self.emailgenerator.setFirstname(prenom)
        print("done")

    def configure_surname(self):
        nom = input("Surname ?\n")
        self.emailgenerator.setSurname(nom)
        print("done")

    def generate_mail(self):
        self.emailgenerator.generateEmails()

    def save_mails_gen(self):
        self.emailgenerator.saveMails()
        print("done")

    def print_templates(self):
        self.emailgenerator.printTemplates()


    ##option menu 2
    def setup_url_scrapp(self):
        url = input("URL ?\n ")
        self.emailscrapper.set_url(url)
        print("done")

    def setup_proxy_scrapp(self):
        proxy = input("Proxy ? (A.A.A.A:1337) ?\n")
        self.emailscrapper.set_proxy(proxy)
        print("done")

    def setup_timeout(self):
        to = input("Timeout ? \n")
        self.emailscrapper.set_timeout(to)
        print("done")

    def save_gathered_mail(self):
        self.emailscrapper.save_mails()
        print("done")


    def run_scrap(self):
        self.emailscrapper.run()

    ##option menu3

    def setup_mail_thrust(self):
        mail = input("mail ? \n")
        if(self.emailthruster is None):
            self.emailthruster = REP.Reputation(mail)
        self.emailthruster.set_mail(mail)
        print("done")

    def setup_proxy_thrust(self):
        if(self.emailthruster is None):
            print("Veuillez renseigné un mail au préalable")
        else:
            proxy = input("Proxy ? (A.A.A.A:1337) ?\n")
            self.emailthruster.set_proxy(proxy)
            print("done")

    def save_mail_info_thrust(self):
        if (self.emailthruster is None):
            print("Veuillez renseigné un mail au préalable")
        else:
            self.emailthruster.save_response()
            print("done")

    def run_thrust(self):
        if (self.emailthruster is None):
            print("Veuillez renseigné un mail au préalable")
        else:
            self.emailthruster.run()
            print("done")

