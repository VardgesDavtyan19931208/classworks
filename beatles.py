text_beatles = {1: "Oh yeah, I'll tell you something", 
				2: "I think you'll understand",
				3: "When I'll say that somethin",
				4: "I want to hold your hand",
				5: "I want to hold your hand",
				6: "I want to hold your hand",
				7: "Oh please, say to me",
				8: "You'll let me be your man",
				9: "And please, say to me",
				10: "You'll let me hold your hand",
				11: "I'll let me hold your hand",
				12: "I want to hold your hand",
				13: "And when I touch you I feel happy inside",
				14: "It's such a feeling that my love",
				15: "I can't hide",
				16: "I can't hide",
				17: "I can't hide"}





user_input = int(input("Please unput the number: "))

if 0 < user_input <= len(text_beatles):
	print(text_beatles[user_input])
else:
	print("The inputed number is bigger that quantity of rows")
