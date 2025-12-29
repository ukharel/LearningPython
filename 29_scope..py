# variable scope :- where variables is accessible and visisble
# scope resolution - It follows LEGO - Local , Enclosed , Global and Built it



# x=35 # Global variable
# def func1():
#     x= 36  # Enclosed Variable
#     def func2():
#         x=25 # Local Variable
#         print(x)
#     func2()

# x=23 # Global Varibale
# func1()

from math import e

def print_e():
    print(e)# e in here is built in variable

e =2.1 # Global variable
print_e()