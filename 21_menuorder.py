
cart =[]
total=0
menu = {
    "Chowmein": 130,
    "Momos":150,
    "Tea": 25,
    "Samosas":50,
    "Coke": 120,
    "Burgers": 150,
    "KattiRool": 160,
    "Sandwich": 180,
    "Pizza": 1050
}


print('------ Menu ------')

for key,value in menu.items():
    print(f'{key:10}:{value:.2f}')

while True:
    food = input('Select an item (q/Q to quit): ')

    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------ YOUR ORDER ------")

for food in cart:
    total += menu.get(food)
    print(food, end=' ')
print()
print(f'Total amount is: Rs{total}')
