# Functions - A reusable block of code 
# It uses () to call the functions

# suppose you want to print " Happy Birthday and write wishes for 20 times. "
# print("Happy Birthday!!!")
# print("May you have prosperous life and family be filles with bless and joy.")

# # You have to copy it 20 times to print for 20 times
# # Instead You can make one function that has all the content for once and call it wherever you need it.

# def say_birthday():
#     print("Happy Birthday!!!!")
#     print("May you have prosperous life and family be filles with bless and joy.")

# say_birthday()
# say_birthday()
# say_birthday()

def say_hello(name):
    print(f'Hello {name}')

say_hello("Bob")
say_hello("Ujjwal")

# Return - A statement that ends the function and return value to the caller.


def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

sum = add(1,3)
print(sum)

subt = sub(1,3)
print(subt)

mult=mul(4,5)
print(mult)

divi = div(4,2)
print(divi)
