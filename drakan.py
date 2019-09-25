name = input("Hello, what`s your name:  ")
print("Hello, " + name + "!!! :) ")

print("I am here to help you to decide what to wear today depending on wheather")
weather = input("So, what`s the temperature in your city: ")
temp = float(weather)
if temp < 10:
	print("It`s very cold, dress like TANK! :D ")
elif temp < 20:
	print("It`s chill, dress warmer :)")
else:
	print("Weather is good, wear what you want!! ")