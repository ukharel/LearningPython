# List Comprehension- It is the alternative way for creating list in the python
# it is compact and easier to undrstand then traditional way of writing.
# Written in the form of :- [Expression for value in iterable if condition ]



# Tradional way

# square= []
# for x in range(1,6):
#     square.append(pow(x,2))
# print(square)


# List comprehension
# square = [x**2 for x in range(1,6)]
# print(square)
 
# in string
# foods= ["Pasta","Pizza","Momos","Chowmein","Noodles"]
# food_with_uppercase = [food.upper() for food in foods ]
# fav_food= [print(f'My fav food is {food}') for food in foods if food=="Noodles" ]
# print(food_with_uppercase)



