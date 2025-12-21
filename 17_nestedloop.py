# Nested Loop - It is Loop inside a loop (outer loop, inner loop)


'''rows = int(input('Enter a number of rows: '))
columns = int(input('Enter a number of columns: '))
symbol = input('Enter a symbol to print: ')

for i in range(rows):
    for j in range(i):
        print(symbol, end='')
    print()
'''
rows=9
for i in range(rows):
    for j in range(rows-i-1):
        print(' ', end='')

    for j in range(2*i+1):
        print("*", end='')
    print()