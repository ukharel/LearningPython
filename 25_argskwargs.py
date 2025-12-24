# Args = it passess the multiple non key argumnets
# Kwargs = it passes the multiple keywords arguments
# * upackin operator


# def summation(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(summation(1,2,3,4,5,6))

# def say_name(**kwargs):
#     for value in kwargs.values():
#         print(value)


# say_name(name1= "ujjwal",
#          name2="Romesh",
#          name3="Biraj")



# Creating shipping label program

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    # for value in kwargs.values():
    #     print(value,end=" ")
    print(f"{kwargs.get('country')} {kwargs.get('city')}")
    print(f"{kwargs.get('street')}")

shipping_label("Mr","Ujjwal","Kharel",
               country="Nepal",
               city= "Jhapa",
               street = "Gajurmukhi tool")