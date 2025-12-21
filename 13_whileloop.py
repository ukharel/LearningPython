# while loop - it execute the code untill the condition remains True

# program to check name if entered or not
name= input('Enter your name? ')

while name == '':
    print('Enter a name.')
    name= input('Enter your name? ')
print(f'Your name is {name}')


cooking_time = int(input('Enter a cooking time: '))

# program for cooking time

while cooking_time > 5:
    print('You are cooking late. ')
    cooking_time = int(input('Enter a cooking time: '))

print(f'Your cooking time should be {cooking_time}')

# program to choose number from 1 to 10.

num = int(input('Enter a number from 1 to 10. '))

while num < 0 or num > 10:
    print('Number must be between 0 to 10')
    num = int(input('Enter a number from 1 to 10. '))
print(f'Your number is {num}')