sum = 0

for i in range(1,4):
	next_number = int(input("Enter number # " + str(i) + ": "))
	sum += next_number

print(sum/3)


text = "Hello World"

for i in text:
	print(i)


some_string = ("hello world", "asdf", "asdasd")
for i in some_string:
	print(i)


i = 0

while i < 10:
	print(i)
	i += 1
