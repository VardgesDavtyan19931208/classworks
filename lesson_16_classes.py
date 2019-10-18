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


class BankAccount:
	def __init__(self, name, balance = 0.0):
		self.log("Account created")
		self.name = name
		self.balance = balance

	def getBalance(self):
		self.log("Balance checked at " + str(self.balance))

	def deposit(self, amount):
		self.balance += amount
		self.log("+" + str(amount)+": " + str (self.balance))

	def withdraw(self, amount):
		self.balance -= amount
		self.log("-" + str(amount) + ": " + str(self.balance))

	def log(self, message):
		print(message)



my_bank_account = BankAccount("Jirayr Melikyan")
my_bank_account.deposit(30.0)
my_bank_account.getBalance()
my_bank_account.withdraw(10.0)
my_bank_account.getBalance()


my_bank_account = BankAccount("Vardges Davtyan")
my_bank_account.deposit(15.0)
my_bank_account.getBalance()
my_bank_account.withdraw(5.0)
my_bank_account.getBalance()

