# Random - it is the pre-built in modules that generate does manythings like genereate random numbers, make choices or do shuffle and many others.
# You need to import in to run into your system.

import random

low_num = 1
high_num = 100

# num = random.randint(low_num,high_num)
# choices= ["Rock","Paper","Scissor"]
# choice= random.choices(choices)
# print(choice)

# alpabhet= ["A","B","C","D"]
# random.shuffle(alpabhet)
# print(alpabhet)

# print(num)


# Rock Paper Scissors Game


choices=["Rock","Paper","Scissors"]


is_running = True

while is_running:
    answer = random.choices(choices)
    user_answer = input('Enter your choice (Rock/Paper/Scissors): ').strip()
    print(f'User chooses {user_answer}')
    for choice in answer:
        print(f'Computer chooses {choice}')
  

    if user_answer == choice:
        print("Tie!!")
    elif user_answer== "Rock" or answer== "Scissors":
        print('You win!!')
    elif user_answer=="Paper" or answer == "Rock":
        print("You win!!")
    elif user_answer == "Scissors" or answer == "Paper":
        print("YOu win!!")
    else:
        print("You Lose")

    is_playing= input("Play Again? (y/n): ").lower()
    if is_playing == 'y':
        is_running= True
    elif is_playing == "n":

        is_running= False
    

   
   
        

