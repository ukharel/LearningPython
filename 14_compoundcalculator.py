# Python Compound Calculator

principle = 0
rate = 0
time = 0

while True:
    principle = int(input('Enter a principle amount: '))
    if principle <=0 :
        print('Principle cannot be less than or equal to zero')
    else:
        break

while True:
    rate = int(input('Enter a rate percentage: '))
    if rate <=0 :
        print('Rate cannot be less than or equal to zero')
    else:
        break

while True:
    time = int(input('Enter a time: '))
    if time <=0 :
        print('Time cannot be less than or equal to zero')
    else:
        break

total = principle * pow((1 + rate/100),time)

print(f'Your balance with {time} year is ${total:,.2f}')

