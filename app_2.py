print("Hello")

First_side_of_triangle = input("Input First side of triangle: ")
Second_side_of_triangle = input("Input Second side of triangle: ")
Third_side_of_triangle = input("Input Third side of triangle: ")

We_can_make_a_triangle = print((int(First_side_of_triangle) + int(Second_side_of_triangle)) > int(Third_side_of_triangle) and (int(First_side_of_triangle) + int(Third_side_of_triangle)) > int(Second_side_of_triangle) and (int(Second_side_of_triangle) + int(Third_side_of_triangle)) > int(First_side_of_triangle) )