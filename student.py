import os


class Student(name="User", phone=None, email=None,current_level=100, final_level=400):
	"""
	Student Profile
	description: Creates and manages the profile of the user
	"""

	def __init__(self, name, phone, email, current_level, final_level):
		self.__username = name
		self.__phone = phone
		self.__email = email
		self.__current_level = current_level
		self.__final_level = final_level
		self.__university_name = None
		self.__department = None

	@property
	def username(self):
		return self.__username
	
	@username.setter
	def username(self, name):
		self.__username = name

	@property
	def phone(self):
		return None
	
	@phone.setter
	def phone(self, phone):
		self.__phone = phone

	@property
	def email(self):
		return self.__email
	
	@email.setter
	def email(self, email):
		self.__email = email

	@property
	def current_level(self):
		return self.__current_level
	
	@current_level.setter
	def current_level(self, level):
		self.__current_level = level

	@property
	def final_level(self):
		return self.__final_level
	
	@final_level.setter
	def final_level(self, level):
		self.__final_level = level

	@property
	def university_name(self):
		return self.__university_name
	
	@university_name.setter
	def university_name(self, name):
		self.__university_name = name

	@property
	def department(self):
		return self.__department
	
	@department.setter
	def department(self, name):
		self.__department = name

	@property
	def save(self):
		try:
			os.chdir(f"./{self.__username}")
		except FileNotFoundError:
			os.mkdir(f"./{self.__username}")
		with open(f"{self.__username}.txt", "w", encoding="utf-8") as f:
			f.write(f"Username={self.__username}\n")
			f.write(f"Phone={self.__phone}\n")
			f.write(f"Email={self.__email}\n")
			f.write(f"University={self.__university_name}\n")
			f.write(f"Department={self.__department}\n")
			f.write(f"Current_Level={self.__current_level}\n")
			f.write(f"Final_level={self.__final_level}\n")


