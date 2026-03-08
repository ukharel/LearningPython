import random

def display_welcome():
    print("=" * 50)  # This creates a line of 50 equals signs
    print("🎯 WELCOME TO THE ULTIMATE GUESSING GAME! 🎯")
    print("=" * 50)
    print("\nGAME MODES:")  # \n creates a new line
    print("1. 🎲 Classic Mode - Guess the number")
    print("2. 🔥 Survival Mode - 3 lives, keep guessing until you lose!")
    print("3. ⚡ Speed Mode - Race against time!")
    print("4. 🃏 Mystery Mode - Random range every round")
    print("5. 🏆 Tournament Mode - Best of 5 rounds")
    print("6. 📊 Practice Mode - Endless with hints")
    print("7. 🤖 Computer Guesses - You think, computer guesses")


def classic_mode():
    print('\n'+'='*40)
    name=input('Enter your name, mr challenger?')
    print(f'Welcome to the game, {name} ')
    mode = input('Enter a mode you want to play (easy,medium,hard)? ').strip()
    if mode == 'easy':
        max_num= 50
        max_attempt=10
        print(' Loading easy mode, choose a number between 1 to 50, have 10 attempts')
    elif mode == 'medium':
        max_num=100
        max_attempt= 7
        print(' Loading medium mode, choose a number between 1 to 100, have 7 attempts')

    elif mode == 'hard':
        max_num= 200
        max_attempt = 5
        print(' Loading difficulty mode, choose a number between 1 to 200, have 5 attempts')

    else:
        print('You have entered invalid difficulty level, defaulting to medium level.')
        max_num= 100
        max_attempt= 7
    secret = random.randint(0,max_num)
    print(secret)
    
    for attempt in range(1, max_attempt+1):
        print(f'Attempts : {attempt}/{max_attempt}.')


        try:
            guess= int(input(f'Enter a guess from 1 to {max_num}.\n'))
        except ValueError:
            print("Invalid number")
        
        if guess == secret:
            points = (max_attempt-attempt+1)*10
            print("\n CORRECT!!")
            print(f'You got it in {attempt} attempts')
            print(f'You have got {points} points')
            return points
        if guess < secret:
            print('Too low. ', end='')

            if secret-guess <= 5:
                print('You are very close!!!')
            else:
                print()

        else:
            print('Too high. ', end= "")

            if secret - guess <=5:
                print('You are vey close!!')
            else:
                print("")

        if attempt == max_attempt/2:
            if secret % 2 ==0:
                print('Hint: Secret number is even. ')
            else:
                print('Hint: Secret number is odd')

    print(f'\n GAME OVER!!, the number was {secret}. ')




def main():
    display_welcome()
    choice = input('Enter a game mode you want to play from 1 to 7? ').strip()

    if choice =="1":
        classic_mode()



main()