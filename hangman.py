import random

win = 0
loss = 0


def game():
    word_list = ['python', 'java', 'swift', 'javascript']
    word = word_list[random.randrange(0, len(word_list))]

    guessed_word = list("-" * len(word))
    guesses = []
    attempts = 8

    while True:
        print()
        if attempts == 0:
            print('You lost!')
            menu(0, 1)
        elif "".join(guessed_word) == word:
            print(word)
            print(f'You guessed the word {word}!')
            print('You survived!')
            menu(1, 0)

        print("".join(guessed_word))
        guess = input('Input a letter: ')
        if len(guess) != 1:
            print('Please, input a single letter.')
        elif guess == "" or guess == " ":
            print('Please, input a single letter.')
        elif guess.isupper() or not guess.isalpha():
            print(
                'Please, enter a lowercase letter from the English alphabet.')
        else:
            if guess in guesses:
                print("You've already guessed this letter.")
            elif guess in word:
                guesses.append(guess)
                for letter in range(0, len(word)):
                    if guess == word[letter]:
                        guessed_word[letter] = guess
            elif guess not in word:
                guesses.append(guess)
                attempts -= 1
                print(
                    f"That letter doesn't appear in the word.  # {attempts} attempts")
            else:
                attempts -= 1
                print(f'No improvements.  # {attempts} attempts')


def results(wins, losses):
    print(f"You won: {wins} times.")
    print(f"You lost: {losses} times")
    menu(0, 0)


def menu(plus, minus):
    global win
    global loss
    win += plus
    loss += minus

    print('Type "play" to play the game, "results" to show the scoreboard,'
          ' and "exit" to quit:')
    option = input().lower()

    if option == 'play':
        game()
    elif option == 'results':
        results(win, loss)
    elif option == 'exit':
        quit()


while True:
    menu(0, 0)
