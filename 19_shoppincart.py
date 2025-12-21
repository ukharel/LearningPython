# Shopping cart python program



gadgets = []
prices = []
total = 0

while True:
    gadget = input('Enter a gadget you want to buy ( q/Q to quit): ')

    if gadget.lower() == 'q':
        break
    else:
        price = float(input('Enter the price of Gadget: '))
        gadgets.append(gadget)
        prices.append(price)

print('------Your Cart--------')
for i in gadgets:
    print(i, end=' ')
for i in prices:
    total +=i
print()
print(f'Your total balance is {total}')