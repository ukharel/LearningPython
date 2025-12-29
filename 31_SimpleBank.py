
def show_balance(balance):
    print(f" Your balance is ${balance}")

def deposit():
    amount = int(input('Enter a amount to deposit : '))
    if amount < 0:
        print("You cannot deposit negative amount")
    elif not str(amount).isdigit():
        print('Please provide valid amount')
    return amount

def withdraw(balance):
    amount = int(input("Enter a amount to withdraw: "))
    if amount < 0:
        print("You cannot withdraw negative amount")
    elif amount > balance:
        print(" You have insufficient balance.")
    elif not str(amount).isdigit():
        print('Please provide valid amount')
    return amount
    


def main():
    balance=0
    is_running = True
    while is_running:
        print("*******************************")
        print("Welcome to the Ujjwal's ATM")
        print("*******************************")
        print("1. Show balance amount ")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("*******************************")

        option_to_choose = input("Choose a option from 1 to 4: ")

        if option_to_choose == '1':
            show_balance(balance)
            print("*******************************")
        if option_to_choose == '2':
            balance += deposit()
            
            print("*******************************")
        if option_to_choose == '3':
            balance -=withdraw(balance)
            print("*******************************")
        if option_to_choose == '4':
            is_running= False
            



if __name__ == "__main__":
    main()
        




