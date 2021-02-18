from os import name
from os import system
import myMenu.process

class Menu:
    def __init__(self):

        self.optionsTier = []
        """
        structure du myMenu déroulé
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
        self.optionsTier.append(["EmailGenerator", "EmailScrapper", "EmailThruster"]) #liste des options du myMenu level0
        self.optionsTier.append(["Renseigner la personne", "Generer des emails", "Sauvegarder les emails", "Afficher les templates"])
        self.optionsTier.append(["URL a scrapper", "Proxy a utiliser","Set le timeout", "Sauvegarder les emails récupérés", "Lancer le scrapping"])
        self.optionsTier.append(["Renseigner l'email", "Proxy a utiliser","Sauvegarder les informations","Lancer l'analyse de confiance"])

        self.pileChoix = [] #en fonction des choix user on retient les choix précedent etc
        #ex : pileChoix = 13 ==> EmailTrhuster - Renseigner l'email

        self.pro = myMenu.process.Process()


    #routine du myMenu
    def run(self):
        stop = False
        while(not stop):
            self.__clear()
            self.__print_menu()
            self.pileChoix.append(int(self.__get_choice())) #on ajoute sur la pile de choix le choix de l'user
            backward = self.__processChoiceQuitting()#on processs le choix
            if(backward and len(self.pileChoix)==1): #on quitte le run car quitter sur tier 0
                stop = True
            else:
                if(backward):#on choisi quitter dans un sous myMenu
                    self.pileChoix.pop()#on depop le choix du backward
                    self.pileChoix.pop()#on remonte d'un tier
                else: #on a fait un choix il faut le process
                    if(len(self.pileChoix)==2):
                        self.__processChoice()
                        self.pileChoix.pop() #on a finit de process on depop le choix

        print("quitting...")


    #process un choix du myMenu qui n'est pas un retour ou quitter
    def __processChoice(self):
        self.pro.cess(self.pileChoix)


    ##return stop=true si y'a l'option quitté a été choisie
    def __processChoiceQuitting(self):
        #on determine si on a selectionné l'option quitter
        if (len(self.pileChoix) == 1):  # premier choix
            quitter = len(self.optionsTier[0])+1
        else:
            quitter = len(self.optionsTier[int(self.pileChoix[0])])+1  # par construction c'est correct
        return int(self.pileChoix[-1]) == int(quitter)

    #affiche la bannière
    def __printBanner(selfs):
        print("\n")
        print("___________ 	          __        ________ ")
        print("\_    _____/ _____ _____ |__|  |  /   _____/ ________________  ______ ______   ___________ ")
        print("|     __)_ /      \\__  \ |  |  |  \_____  \_/ ___\_  __ \__   \ \____ \\____ \_/ __ \_  __ \ ")
        print("|         \  Y Y  \/ __ \|  |  |__/        \  \___|  | \// __ \|  |_> >  |_> >  ___/|  | \/")
        print("/_______  /__|_|  (____  /__|____/_______  /\___  >__|  (____  /   __/|   __/ \___  >__|   ")
        print("        \/      \/     \/                \/     \/           \/|__|   |__|        \/       ")
        print("\n\n\t\t\t\tby Kr0wZ&314wind\n")

    #affiche les options def dans le constructeurs
    def __printOptions(self):
        i=1
        #on determine quels options il faut afficher :
        if(len(self.pileChoix)==0): #premier choix
            tier = 0
        else:
            tier = self.pileChoix[0] #par construction c'est correct
        for option in self.optionsTier[int(tier)]:#on affiche les options dans le tier myMenu en fonction des choix
            print(i,".", option)
            i+=1
        if(tier!=0):
            print(i,". Retour")
        else:
            print(i,". Quitter")

    #affiche le myMenu
    def __print_menu(self):
        self.__printBanner()
        self.__printOptions()

    #recupère le choix de l'utlisateur
    def __get_choice(self):
        choice = '99'
        tier = len(self.pileChoix) #on recupere le niveau dans les menus via le choix
        if(tier != 0):
            menu = self.pileChoix[tier-1] #on recup le menu
        else:
            menu = 0
        try:
            while (int(choice) > len(self.optionsTier[menu])+1):
                choice = input(">")
                #todo on peut afficher a nouveau les options ici
        except ValueError:
            self.__get_choice()
        return choice

    #clear l'output
    def __clear(self):
        if name == 'nt':
            print("exec cls")
            system('cls')
        else:
            print("exec clear")
            system('clear')

if (__name__=="__main__"):
    m = Menu()
    m.run()