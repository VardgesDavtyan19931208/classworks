# #def function name():
# 	#return

# def add_to_numbers(num1,num2):
# 	num1 = int(num1)
# 	num2 = int(num2)
# 	return num1 + num2


# first = 1
# second = 2
# third = 3


# print(add_to_numbers(first,second), add_to_numbers(second,third))


# print("Hello, I will help you to count the volume of prizm :))) ")


# def prizm(num1,num2,num3):
	
# 	return num1*num2*num3


# lenght = int(input("input the lenght: "))
# weight = int(input("input the weight: "))
# height = int(input("input the height: "))


# print("The volume of prizm is",prizm(lenght,weight,height),"m^3")


# def validate_input(some_input):
# 	if type(some_input) == int:
# 		return True
# 	else:
# 		return False

# while True:
# 	user_input = input("Enter a integer")
# 	print(validate_input(user_input))
# 	if validate_input(user_input):
# 		break

# print(user_input)


# number = input("enter your number: ")

# def even_or_odd(number):
# 	if number % 2 == 0:
# 		return "even"
# 	return "odd"

# print(even_or_odd(int(number)))


# def two_numbers(num1,num2):
# 	return num1+num2

# print(two_numbers(1,2))


# print("string", "string2", end = "")
# print("string" + "\n" + "string2")


# def currency_amount(amount, currency="USD"):
#     amount = str(amount)
#     if currency == "JPY":
#         return "¥" + amount
#     elif currency == "USD":
#         return "$" + amount    
#     elif currency == "EUR":
#         return "€" + amount
#     else:
#         return amount
# print(currency_amount(5, "JPY"))



my_balance = int(input("Input your balance: "))

def check_balance(num1,num2):
	return num1+num2

price = int(input("Input the price: "))
tax = int(input("Input the price: "))

if check_balance(price, tax) > my_balance:
	print("Go back home :( ")
else:
	print("Buy it!")












