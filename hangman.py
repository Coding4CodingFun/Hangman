import random

def hangman(word):
    wrong = 0
    stages = ["",
             "_______     ",
             "|           ",
             "|      |    ",
             "|      0    ",
             "|     /|\   ",
             "|     / \   ",
             "|           ",
              ]
    remaining_letters = list(word)
    board = ["_"] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrong < len(stages):
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in remaining_letters:
            cind = remaining_letters.index(char)
            board[cind] = char
            remaining_letters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print("The word was " + " ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose!  It was {}.".format(word))


guess_list = ['cat','dog', 'farm', 'truck', 'school', 'desk', 'computer', 'dictionary']

hangman(random.choice(guess_list))
