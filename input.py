# input - it prompts the user to insert a data and return string as value

name = input('Enter your name? ')
age = int(input(' Enter your age? '))
age = age + 1

print(f' Hello, {name}')
print("Happy birthday")
print(f'You are now {age}')

# Area of rectangle

length = float(input('Enter a length ? '))
width = float(input('Enter a width? '))
area = length * width
print(f' The total area is {area} cm^2')