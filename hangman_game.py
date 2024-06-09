def get_location_of_char(word , char):
    locations = []
    for index, anychar in enumerate(word):
        if anychar == char:
            locations.append(index)
    return locations


def hangman():
    words = {'kiwi','orange','banana','apple'}
    while True:
        choice = input("Please enter p for play, e for exit")
        if choice == "p":
            name = input("Please enter your name")
            print(f"**** welcome {name} to our hangman game")
            if words:
                select_word = words.pop()
                # print(select_word)
                print(f"Guess the word that consists of {len(select_word)*'-'} letters")
                guessword = ['-']*len(select_word)
                # print(guessword)
                for i in range(1, 8):
                    char = input("Guess a letter")
                    # print(char)
                    char_location = get_location_of_char(select_word, char)
                    print(char_location)
                    if char_location:
                        for index in char_location:
                            guessword[index] = char

                    # print(''.join(guessword))
                    if ''.join(guessword) == select_word:
                        print("---Congratulations You won the game---")
                        break
                    # check location of char in the string ?  Then replace it in the guessed word
                else:
                    print("--- you have lost the game ----")
            else:
                print("--- you have completed all levels")
                exit()

        elif choice == "e":
            exit()
        else:
            print("--- try enter pleaee enter p for play, e for exit")


if __name__ == "__main__":
    # hangman()
    # res=get_location_of_char('banana', 'a')
    # print(res)
    pass


import math