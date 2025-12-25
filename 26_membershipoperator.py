# Membership Operator : It test the value or variables if it exsit in the sequences.
# in and not in operators
# It woorks in (string, list, tuples, set, and dictionary)


# String

# food = "Hotdog"

# letter = input("Enter a letter in a secret word: ")
# if letter in food:
#     print(f"{letter} letter exist in food")
# else:
#     print(f'{letter} was not found. ')


lst= ["Ram","Hari","Sita","Krishna","Shiva","Binod","Ujjwal"]

word= input("Guess a word in the list: ")

if word in lst:
    print(f'{word} is there in the list.')
else:
    print(f'{word} was not found. ')


my_dictionary = {"Ujjwal":"Kharel",
                 "Binod":"Chaudary",
                 "Biraj":"Pathak",
                 "Karan":"Bhatta"}

name = input("Enter a name: ")
if name in my_dictionary:
    print(f"{name}'s caste is {my_dictionary[name]}")
else:
    print(f"{name} was not found. ")