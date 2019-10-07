try:

	input_file = open("NumberFile.txt", mode = "r")

	try:
		for line in input_file:
			print(int(line))

	except ValueError:
		print("A value error occured")

	else:
		print("No errors occured")

	finally:
		input_file.close()

except IOError:
	print("An error occured reading the file")