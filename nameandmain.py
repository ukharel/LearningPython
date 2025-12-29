# if __name__ == "__main__" --> it executes the program standalone or when the attribute __name__ == "__main__".
# Initially, the value of name is main meaning the program will execute the code of that program only. If create another file and try to import some function from this 
# file that it will provide you the specific function only if you have inserted __name__ == "__main__" this, else it might run the all the code on another file


def add(a,b):
    return a + b
def mult(a,b):
    return a*b


# print(f"The addition is {add(2,3)}")   # when i left like this without main, then when it is imported in another file, this block also get executed
# print(f"The multiply is {mult(2,3)}")
if __name__ == "__main__": # this evaluates to True here, but false in another file
    print(f"The addition is {add(2,3)}")# when you do this, only the function call is executed
    print(f"The multiply is {mult(2,3)}")
