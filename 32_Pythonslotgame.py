import random
def show_row():
    symbols= ['🍒','🍎','🥕','🥭','⭐']
    result = [random.choice(symbols) for symbol in range(3)]
    return result

def print_row(row):
    print("   ".join(row))

    

def give_payout(row,bet):
    if row[0]==row[1]== row[2]:
        if row[0]=='🍒':
            return bet * 10
        elif row[0]=='🍎':
            return bet * 20
        elif row[0]=='🥕':
            return bet * 30
        elif row[0]=='🥭':
            return bet * 40
        elif row[0]=='⭐':
            return bet * 50
    return 0

def main():
    balance=100
    while balance > 0:
        print("**********************")
        print("Welcome to the Python Slot Game")
        print("**********************")
        print("Symbol : 🍒 🍎 🥕 🥭 ⭐")
        print("**********************")
        bet = (input("Enter a amount you want to bet: "))
        if bet.isalpha():
            print('Bet must be digits')
            print()
            print()
            continue
        if int(bet) < 0:
            print('Bet cannot be negative. ')
            print()
            print()
            continue
        if int(bet) > balance:
            print("Insufficient funds")
            print()
            print()
            continue
        balance -=int(bet)
        row = show_row()
        print_roww=print_row(row)
        print(f"Your balance is {balance}")
        pay_out= give_payout(row,bet)
        if pay_out > 0:
            print(f'You won ${pay_out}')
        else:
            print('You lose this round. ')

        balance += pay_out
        play_again = input("Do you want to play again (Y/N): ").upper()
        if play_again != "Y":
            break
        
        print("************************")
        print(f'Your final balance is ${balance}')
        print("************************")

main()