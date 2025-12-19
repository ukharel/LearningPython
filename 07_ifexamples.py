#Python basis calculator

'''operator = input('Enter a operator (+,-,*,/): ')
num1 = int(input('Enter a numberOne? '))
num2 = int(input('Enter a numberTwo? '))

if operator == "+":
    print(f'The sum is {num1 + num2}')
elif operator == "-":
    print(f'The subtraction is {num1 - num2}')
elif operator == "*":
    print(f'The multiplication is {num1 * num2}')
elif operator == "/":
    print(f'The divison is {num1 / num2}')
else:
    print(f'{operator} is not valid')'''

# weight converter

weight = float(input('Enter a weight: '))
unit = input('Enter a Pound or Kilos (P/K): ')

if unit == "P":
    print(f'The weight in pound is {weight * 2.205} pounds.')

elif unit == "K":
    print(f'The weight in kilo is {weight / 2.205} Kg. ')
else:
    print(f'{unit} is not valid. ')