# class Person:
# 	def __init__(self, first_name, last_name, eye_color):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.eye_color = eye_color

# my_person = Person("Jirayr", "Melikyan", "Green")


# print(my_person.first_name)
# print(my_person.last_name)
# print(my_person.eye_color)


# my_person2 = Person()


# class BankAccount:
# 	def __init__(self, name, balance = 0.0):
# 		self.log("Account created")
# 		self.name = name
# 		self.balance = balance

# 	def getBalance(self):
# 		self.log("Balance checked at " + str(self.balance))

# 	def deposit(self, amount):
# 		amount = input("input money for deposit: ")
# 		self.balance += int(amount)
# 		self.log("+" + str(amount)+": " + str (self.balance))

# 	def withdraw(self, amount):
# 		amount = input("input money for withdraw: ")
# 		self.balance -= int(amount)
# 		self.log("-" + str(amount) + ": " + str(self.balance))

# 	def log(self, message):
# 		print(message)



# my_bank_account = BankAccount("Jirayr Melikyan")
# my_bank_account.deposit(0)
# my_bank_account.getBalance()
# my_bank_account.withdraw(0)
# my_bank_account.getBalance()


# class Person:
#     def __init__(self, name, eyecolor, age):
#         self.name = name
#         self.eyecolor = eyecolor
#         self.age = age

# my_person1 = Person("Arman Babayan", "Green", 37)

# my_person2 = Person("Arman Babayan", "Green", 37)

# print(my_person1.name)
# print(my_person2.name)

# my_person1.name = "aaa"

# print(my_person1.name)
# print(my_person2.name)


class Name:
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name

class Person:
	def __init__(self, name, eyecolor, age):
		self.name = name
		self.eyecolor = eyecolor
		self.age = age


my_name = Name("Jirayr", "Melikyan")

my_person = Person(my_name, "Brown", 19)

def capitalize_name(name):
	name.first_name = name.first_name.upper()
	name.last_name = name.last_name.upper()

capitalize_name(my_name)
