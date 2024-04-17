import random
from words import word_list

def main():
    log_in()
    print_rules()
    

def log_in():
    """
    Function that asks user for their name and greets them to the game.
    """

    name = input("\nPlease enter your name: \n")
    print(f"\nHello {name} and welcome to WordGuesser\n")

def print_rules():
    """
    Function that prints the rules and game explanation.
    """

    print("WordGuesser is a game like Hangman, just less cruel.\n")
    print("The game works as following:\n")
    print("1. You need to try and guess the word, letter by letter.")
    print("2. With each try, you will put in a single letter ")
    print("   that you think is contained in the word.")
    print("3. If the letter you provided is contained in the word,")
    print("   the game is going to show you in which position it is.")
    print("   If the word does not contain the letter, your try ")
    print("   counts as a fail.")
    print("3. You only have 6 tries, or you loose the game.\n")



main()