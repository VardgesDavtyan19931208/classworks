# user_text = input("Unput the text: ")

# sign = ord("!")
# count = 0

# for m in user_text:
# 	if ord(m) == sign:
# 		count += 1
# print("You have ", count, "<!>-s")

# if count == 0:
# 	print("You dont have <!>")


# a = 'homeless'

# print(a[-5:-2])


# my_string = "this is MY test string!"


# print(my_string)
# print(my_string.capitalize())
# print(my_string.lower())
# print(my_string.upper())
# print(my_string.title())
# print(my_string.replace("MY", "YOUR"))


def get_middle_three_chars(sample_str):
	middle_index = int(len(sample_str)/2)
	print("Original String is", sample_str)
	middle_three = sample_str[middle_index-1:middle_index+2]
	print("Middle three chars are", middle_three)

print(get_middle_three_chars("JhonDipPeta"))
print(get_middle_three_chars("Jasonay"))