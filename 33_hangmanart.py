import random

words= ["goat","rat","elephant","rose","yellow","mother","father","career","computer","artificial","intelligence","python"]

hangman_art= {
    0:('      ',
       '      ',
       '      '),
    1:('  o   ',
       '      ',
       '      '),
    2:('  o   ',
       '  |   ',
       '      '),
    3:('  o   ',
       ' /|   ',
       '      '),
    4:('  o   ',
       ' /|\\ ',
       '      '),
    5:('  o   ',
       ' /|\\ ',
       ' /    '),
    6:('  o   ',
       ' /|\\ ',
       ' / \\ ')
}

def show_man(wrong_guess):
    print("****************")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("****************")

def show_hint(hint):
    print(' '.join(hint))

def show_answer(answer):
    print(' '.join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    guessed=0
    guessed_answer=set()
    is_running = True
    while is_running:
        show_man(guessed)
        show_hint(hint)
        # show_answer(answer)
        guess= input('Enter your guessed letter: ').lower()

        if len(guess) !=1 or not guess.isalpha():
            print("Invalid input")
            continue
        if guess in guessed_answer:
            print(f"{guess} already exist. ")
            continue
        guessed_answer.add(guess)


        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
        else:
            guessed +=1
        if "_" not in hint:
            show_man(guessed)
            show_hint(hint)
            print("YOU WIN!!!")
            is_running=False

        elif guessed >= len(hangman_art)-1:
            show_man(guessed)
            show_hint(hint)
            show_answer(answer)
            print("YOU LOSE!!!")
            is_running=False

if __name__=="__main__":
    main()

