
petrol_in_machine = 0

petrol_in_conteiner = 2

petrol_in_bottle = 1

use_petrol_that_in_conteiner_or_bottle = petrol_in_machine < petrol_in_conteiner or petrol_in_machine < petrol_in_bottle

if use_petrol_that_in_conteiner_or_bottle == True:
	print("Use that")
else:
	print("Go home and sleep")


box_form = "square"

box_color = "black"

form_of_item_inside_box = "round"

what_is_inbox = "orange"


user_box_form = input("What form does your box have?: ")
user_box_color = input("Which color is your box?: ")
user_box_item_form = input("Which form does item have?: ")

orange = ((box_form == user_box_form and box_color == user_box_color) and (box_form == user_box_form and form_of_item_inside_box == user_box_item_form))

Print("what_is_inbox")