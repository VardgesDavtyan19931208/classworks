#students_exam = {'Gor Smbartyan': 26, 'David Grigoryan': 26, 'Vardges Hovhannisyan': 26, 'Rafayel Kostanyan': 28,'Khachatur Khachatryan': 23, 'Marat Yarumyan': 24, 'Artur Altunyan': 28,
# 'Sedrak Harutyunyan': 24; 'Marianna Beglaryan': 25, 'Vardges Davtyan': 28, 'Tigran Danielyan': 28,'Arno Gevorgyan': 23, 'Artur Ananyan': 28, 'Arman Babayan': 28}

# students_exam = {'Gor Smbartyan': 26, 'David Grigoryan': 26}

# students_exam['Gor Smbartyan'] = 32

# print(students_exam.keys())
# print(students_exam.values())


# EX:4
# classes = {"Math": ["David", "Lucy", "Dana"],
# 			"Physics": ["Addison", "Benjamin"],
# 			"Chemistery": ["Sara","Pele"]}

# print("Students in math class", classes["Math"])

# classes["Math"].append("Jirayr")

# print("Students in math class", classes["Math"])


sample_text = "One morning when Gregor Samsa woke from troubled dreams he found himself transformed in his bed into a horrible vermin He lay on his armour-like back and if he lifted his head a little he could see his brown belly slightly domed and divided by arches into stiff sections The bedding was hardly able to cover it and seemed ready to slide off any moment His many legs pitifully thin compared with the size of the rest of him waved about helplessly as he looked Whats happened to me? he thought It wasn't a dream His room a proper human room although a little too small lay peacefully between its four familiar walls A collection of textile samples lay spread out on the table - Samsa was a travelling salesman - and above it there hung a picture that he had recently cut out of an illustrated magazine and housed in a nice gilded frame It showed a lady fitted out with a fur hat and fur boa who sat upright raising a heavy fur muff that covered the whole of her lower arm towards the viewer Gregor then turned to look out the window at the dull weather Drops"

words_dict = {}
sample_text = sample_text.lower()
sample_text = sample_text.replace(',', '')
sample_text = sample_text.replace('.', '')
sample_text = sample_text.split(' ')



for word in sample_text:
	if word in words_dict.keys():
		words_dict[word] += 1
	else:
		words_dict[word] = 1

print(words_dict.items())


# for (word,amount) in words_dict.items():
# 	if amount > 2:
# 		print(word, '.', amount)