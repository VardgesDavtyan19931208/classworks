
# range_user = range(5,15)

# number_by_user = int(input("input number: "))

# try:
# 	for number_by_user in range_user:
# 		if number_by_user > 10:
# 			print("!!!")
# except:
# 	print("error occurred")



my_string = "This string is not number"

try:
	print("Converting my string to int...")
	print("String #" + 1 + ": " + my_string)
	my_int = int(my_string)
	print(my_int)
except ValueError:
	print("Can`t convert; my_string to a number")
except TypeError:
	print("Can`t concatinate number with string")

print('Done!')