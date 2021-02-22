import copy
#import test
import connector as con

class Menu:

	def __init__(self):
		myfunc = con.Connector()
		self.menu = {
			"1": ("Email Generator", {
				"1": ("Configure", {
					"1": ("Configure firstname", myfunc.configure_firstname),
					"2": ("Configure surname", myfunc.configure_surname)
				}), #getattr(test.Test, "print_func")("my_arg")
				"2": ("Generate mails", myfunc.generate_mail),
				"3": ("Save generated mails", myfunc.save_mails_gen),
				"4": ("Print templates", myfunc.print_templates),
				"5": ("Return", None)
			}),
			"2": ("Email Scrapper", {
				"1": ("Set up the URL", myfunc.setup_url_scrapp),
				"2": ("Set up the proxy", myfunc.setup_proxy_scrapp),
				"3": ("Set up the timeout (in s)", myfunc.setup_timeout),
				"4": ("Save the gathered mails", myfunc.save_gathered_mail),
				"5": ("Run the scrapping", myfunc.run_scrap),
				"6": ("Return", None)
			}),
			"3": ("Email Thruster", {
				"1": ("Set up the mail", myfunc.setup_mail_thrust),
				"2": ("Set up the proxy", myfunc.setup_proxy_thrust),
				"3": ("Save the information", myfunc.save_mail_info_thrust),
				"4": ("Run the thrusting module", myfunc.run_thrust),
				"5": ("Return", None)
			})
		}

		#Check level of menu with number of items in list
		self.history = []
		self.temp_menu = copy.copy(self.menu)


	def top_level_menu(self):
		for number in sorted(self.menu.keys()):
			print(number + ": " + self.menu[number][0])

	def get_last_item(self):
		return self.history[-1:][0]

	def print_current_menu(self):
		if(isinstance(self.temp_menu, dict)):
			for number in sorted(self.temp_menu.keys()):
				print(number + ": " + self.temp_menu[number][0])
		else:
			self.top_level_menu()

	def get_choices(self):
		return self.temp_menu.keys()

	def update_menu(self):
		if(len(self.history) != 0):
			#We reset the temp_menu
			self.temp_menu = copy.copy(self.menu)
			for level in self.history:
				#Update the temp_menu by browsing history from the top to the bottom
				self.temp_menu = self.temp_menu[level][1]
		#If we're on top of menu then update temp_menu as base menu
		else:
			self.temp_menu = self.menu

	def select_correct_menu(self):
		menu_choice = self.get_last_item()
		#temp_menu is the menu from the user choice and everything below

		#Bug here when too depth
		self.temp_menu = self.temp_menu[menu_choice][1]
		#If temp_menu is not a dict it means we are on a leaf of a branch
		if(not isinstance(self.temp_menu, dict)):
			if(self.temp_menu == None):
				#Pop last value of history (2 times because of current and previous item -> return)
				self.history.pop(-1)
				#If no more history then exit program
				if(len(self.history) != 0):
					self.history.pop(-1)
				else:
					exit()

				self.update_menu()
			else:
				print("Calling function")
				self.temp_menu()
				exit()

		self.print_current_menu()

	def ask_user_input(self):
		while(True):
			#Make validations on user input
			choice = input("> ")
			if(self.verify_user_input(choice)):
				self.history.append(choice)
				self.select_correct_menu()
			else:
				print("Incorrect choice")
				continue


	def verify_user_input(self, user_input):
		available_choices = self.get_choices()
		return user_input in available_choices

	def print_test(self):
		print("This is a test")


if(__name__ == "__main__"):
	menu = Menu()
	#test.print_func("my_arg")
	menu.print_current_menu()
	menu.ask_user_input()
	


# menu.get("2", [None])[1]["1"][1]()