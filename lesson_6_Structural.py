#lesson_6_Structural

#Conditionals

My_num1 = 8
My_num2 = 4
My_num3 = 5

if My_num1 < My_num2 and My_num1 < My_num3:
	print("First value is the least")

if My_num1 > My_num2 and My_num1 > My_num3:
	print("First value is the greatest")


weather = "hot"

money = 90
pool_price = 45

len_of_weather = len(weather)

if weather == 'hot' and money > pool_price and len_of_weather == 3:
	print('go to the pool')
	if money >= 90:
		print ("Invite a girl to go with you")


print('have fun')


#scope

if 5 < 7:
	result = True
	print(result)
print(result)


#if else

a = 10
b = 13

if a < b:
	print('a < b')
else:
	print('a is not less than b')

#else if

a = 18
b = 18

if a > b:
	print('a > b')
elif a < b:
	print('a < b')
else:
	print('a=b')














