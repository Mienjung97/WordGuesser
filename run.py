import random
import time
from words import word_list

def pause(u):
    """
    Function to delay print statements adn takes a float as delay
    in seconds.
    """
    time.sleep(u)

def log_in():
    """
    Function that asks user for their name and greets them to the game.
    """
    name = input("\nPlease enter your name: \n")
    print("-"*23)
    print(f"\nHello {name} and welcome to WordGuesser\n")
    pause(1)

def print_rules():
    """
    Function that prints the rules and game explanation.
    """
    print("-"*56, "\n")
    print("WordGuesser is a game like Hangman, just less cruel.\n")
    pause(2)
    print("The game works as following:\n")
    pause(0.5)
    print("1. You need to try and guess the word, letter by letter.\n")
    pause(0.5)
    print("2. With each try, you will put in a single letter ")
    print("   that you think is contained in the word.\n")
    pause(0.5)
    print("3. If the letter you provided is contained in the word,")
    print("   the game is going to show you in which position it is.")
    print("   If the word does not contain the letter, your try ")
    print("   counts as a fail.\n")
    pause(0.5)
    print("6. You only have 6 tries, or you loose the game.\n")
    print("-"*56, "\n")
    pause(1)

def get_word():
    """
    Get a random word from the "word_list" file and returns it in
    lower case (for further validation)
    """
    word = random.choice(word_list)
    return word.lower()
        
def restart_question():
    """
    This function will ask the user if they would like to restart the game
    or exit the program. Error handleing for wrong input is included.#
    """
    y = input("Would you like to restart the game? (Y/N)\n")
    if y.lower() == "y":
        print("\n")
        print("-"*56, "\n")
        new_word = get_word()
        run_game(new_word)
    elif y.lower() == "n":
        print("Thanks for playing the game!")
    else:
        print("Please enter a valid input.")
        return restart_question()

def guessed_letter_check():
    """
    This function asks the user for the input and only returns it to the 
    "run_game" function after validating that it is only a single letter from
    the alphabet and no letters or signs.
    """
    i = input("\nTake your guess: \n")
    if len(i) == 1:
        if i.isalpha():
            print('i is alpha')
            return i
        else:
            print("Please enter only letters, no numbers.")
            return guessed_letter_check()
    elif len(i) != 1:
        print("Please enter only one letter.")
        return guessed_letter_check()
        

def print_correct(i,word, new_list):
    """
    Gets the correct letter passed by "run_game", searches for its 
    position in the word to guess and prints it accordingly to the 
    console.
    """
    pause(0.5)
    # Idea for how to create the pos_list comes from:
    # https://stackoverflow.com/questions/56324522/program-in-python-to-show-letters-guessed-in-a-hangman-game-not-working
    pos_list = new_list
    for char in word:
        print(f"\nCongratulations! {i} is in the word!\n")
        position = word.find(i)
        pos_list[position] = i
        print (' '.join(pos_list), "\n")
        break
    
def run_game(word):
    """
    Function that runs the main game: It calls functions to check the user input and
    compares it to the word in question.
    If the letter is in the word, the game progresses (more needs to be implemented)
    If the letter is not in the word, the try counter will be decreased.
    If all tries are used up, the player can choose to either start a new game
    or quit
    """
    tries = 6
    current_word = word
    pos_list = ['_' for x in range(len(word))]
    print(word)
    print(f"\nThe word has {len(word)} letters:\n")
    print("_ "*len(word))
    while tries > 0:
        x = guessed_letter_check()
        while True:
            if x in current_word:
                print_correct(x, word, pos_list) 
                print(f"You still have {tries} tries left.\n")
                break
            elif x not in current_word:
                print(f"\nSorry, {x} is not part of the word.")
                tries -= 1
                print(f"You have {tries} tries left.\n")
                break
            elif ValueError:
                break
    else:
        print("You are out of tries and lost!")
        restart_question()


def main():
    """
    Main function that calls every function that is needed for the game.
    """
    #log_in()
    #print_rules()
    word = get_word()
    run_game(word)

main()
