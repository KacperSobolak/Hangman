import os
from string import ascii_lowercase

hangman = ["\n\n\n\n\n",
           "\n\n\n\n\n---",
           "|\n|\n|\n|\n|\n---",
           "|-----\n|\n|\n|\n|\n---",
           "|-----\n|    |\n|\n|\n|\n---",
           "|-----\n|    |\n|    o\n|\n|\n---",
           "|-----\n|    |\n|    o\n|    |\n|\n---",
           "|-----\n|    |\n|    o\n|   -|\n|\n---",
           "|-----\n|    |\n|    o\n|   -|-\n|\n---",
           "|-----\n|    |\n|    o\n|   -|-\n|   /\n---",
           "|-----\n|    |\n|    o\n|   -|-\n|   / \ \n---\nPrzegrałeś"]


def set_clue():
    global sentence
    global hide_sentence
    sentence = input("Podaj hasło do odgadnięcia: \n")
    hide_sentence = []
    for index, char in enumerate(sentence):
        if char.lower() in ascii_lowercase:
            hide_sentence.append("-")
        else:
            hide_sentence.append(char)


def show_hangman(misses):
    print(hangman[misses])


def check_answer(letter):
    if letter in sentence.lower():
        unhide_letter(letter)
        return True
    return False


def unhide_letter(letter):
    global hide_sentence
    for index, char in enumerate(sentence):
        if char.lower() == letter:
            hide_sentence[index] = char


def check_win():
    if "".join(hide_sentence) == sentence:
        return True
    return False


def game():
    set_clue()
    misses = 0
    while misses < len(hangman):
        os.system("cls")
        show_hangman(misses)
        if misses == len(hangman) - 1:
            break
        print("".join(hide_sentence))
        if check_win():
            print("Gratulacje wygrałeś")
            break
        char = input("Podaj litere: ")
        if not check_answer(char):
            misses += 1
    if input("\nCzy chcesz zagrać ponownie? y/n\n") == "y":
        os.system("cls")
        game()


if __name__ == "__main__":
    game()
