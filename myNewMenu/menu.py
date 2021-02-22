import copy
import test

class Menu:
	def __init__(self):
		self.menu = {
			"1": ("First option, first menu", { 
					"1": ("First option, second menu", self.my_function1), #getattr(test.Test, "print_func")("my_arg")
					"2": ("Second option, second menu, first option", self.my_function2),
					"3": ("Third option, configure things", {
						"1": ("Configure name", self.config_name),
						"2": ("Configure surname", self.config_surname),
						"3": ("Submenu (again)", {
							"1": ("My best menu", self.config_surname),
							"2": ("Wow again ???", {
								"1": ("Hope this is last...", test.print_func),
								"2": ("Return", None)
							}),
							"3": ("Return", None)
						}),
						"4": ("Return", None)
					}),
					"4": ("Return", None)
			}),
			"2": ("Second option, first menu", { 
					"1": ("First option, second menu, second option", self.my_function3),
					"2": ("Return", None)
			}),
			"3": ("Quit", None)
		}

		#Check level of menu with number of items in list
		self.history = []
		self.temp_menu = copy.copy(self.menu)

	def my_function1(self):
		print("This is my function1 which is called from " + self.__class__.__name__)

	def my_function2(self):
		print("This is my function2 which is called")

	def my_function3(self):
		print("This is my function3 which is called")

	def config_name(self):
		print("Function to configure name")

	def config_surname(self):
		print("Function to configure surname")

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



if(__name__ == "__main__"):
	menu = Menu()
	#test.print_func("my_arg")
	menu.print_current_menu()
	menu.ask_user_input()
	


# menu.get("2", [None])[1]["1"][1]()