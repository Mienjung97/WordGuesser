import random
import time
import re
from words import word_list, MAX_TRIES

guessed_letters = []
game_counter = 1

def print_line():
    """
    Add 65 dashes to form a line
    """
    print("_"*65, "\n")

def pause(u):
    """
    Function to delay print statements adn takes a float as delay
    in seconds.
    """
    time.sleep(u)

def paused_print_1(print_txt):
    """
    Combines the pause (1s) and print functions for readability.
    """
    print(print_txt)
    pause(1)

def paused_print_05(print_txt):
    """
    Combines the pause (0.5s) and print functions for readability.
    """
    print(print_txt)
    pause(0.5)

def paused_print_2(print_txt):
    """
    Combines the pause (2s) and print functions for readability.
    """
    print(print_txt)
    pause(2)

def take_user_name_input():
    """
    Function that asks user for their name and greets them to the game,
    additionally limits the lenght of the name to 23 characters.
    Info: Any character is allowed in case one wants to use their
    username instead of real name - or X Æ A-12 Musk (Son of Elon Musk)
    would like to play.
    """
    name = input("\nPlease enter your name: \n")
    while len(name) <= 23:
        break
    else:
        print("\nYour name is too long for this program.")
        print("Please make it shorter.\n")
        return take_user_name_input()
            
    print("-"*23)
    paused_print_1(f"\nHello {name} and welcome to WordGuesser\n")
    return name

def print_rules(name):
    """
    Function that prints the rules and game explanation.
    """
    print_line()
    print("WordGuesser is a game like Hangman, just less cruel:")
    print("Instead of hanging a man, you will race against the fuel")
    paused_print_2()"in your racear to try and finish the race.\n")
    paused_print_05("The game works as following:\n")
    paused_print_05("1. You need to try and guess the word, letter by letter.\n")
    print("2. With each try, you will put in a single letter ")
    paused_print_05("   that you think is contained in the word.\n")
    print("3. If the letter you provided is contained in the word,")
    print("   the game is going to show you in which position it is")
    paused_print_05("   and your racecar moves forward.\n")
    print("4. If the word does not contain the letter, your try ")
    paused_print_05("   counts as a fail and reduces the fuel that you have left.\n")
    paused_print_05("5. You only have 6 tries, or you loose the game.\n")
    print(f"6. Have fun, {name}, and try to win as many races as possible!\n")
    print_line()
    pause(1)
    input("Press the Enter key to start!")
    print("\n")

def get_word():
    """
    Get a random word from the "word_list" file and returns it in
    lower case (for further validation)
    """
    word = random.choice(word_list)
    return word.lower()
        
def restart_question(name):
    """
    This function will ask the user if they would like to restart the game
    or exit the program. Error handleing for wrong input is included, as well
    as clearing the list of duplicate inputs.
    """
    global game_counter
    y = input(f"{name}, would you like to restart the game? (Y/N)\n")
    if y.lower() == "y":
        game_counter += 1
        print("\n")
        print_line()
        print(f"{name}, this is your Game no. {game_counter}! Have fun!") #{game_counter}
        guessed_letters.clear()
        new_word = get_word()
        run_game(new_word, name)
    elif y.lower() == "n":
        print(f"Thank you for playing the game, {name}!")
        print_line()
        exit()
    else:
        print("Please enter a valid input.")
        print_line()
        return restart_question(name)

def guessed_letter_check():
    """
    This function asks the user for the input and only returns it to the 
    "run_game" function after validating that it is only a single letter from
    the alphabet and no letters or signs.
    """

    i = input("\nTake your guess: \n").lower()
    if len(i) == 1:
        if i.isalpha():
            if i in guessed_letters:
                print(f"The letter {i} already has been guessed by you.")
                print("Please try again!")
                return guessed_letter_check()
            else:
                guessed_letters.append(i)
                return i
        else:
            print("Please enter only letters, no numbers.\n")
            print_line()
            return guessed_letter_check()
    elif len(i) != 1:
        print("Please enter only one letter.\n")
        print_line()
        return guessed_letter_check()
        
def print_correct(i,word, new_list, tries, name):
    """
    Gets the correct letter passed by "run_game", searches for its 
    position in the word to guess and prints it accordingly to the 
    console.
    """
    pause(0.5)
    # Idea for how to create the pos_list and how to use it comes from:
    # https://stackoverflow.com/questions/56324522/program-in-python-to-show-letters-guessed-in-a-hangman-game-not-working
    pos_list = new_list
    for char in word:
        pause(0.5)
        print(f"\nCongratulations! {i} is in the word!\n")
        positions = [m.start() for m in re.finditer(i, word)]
        for pos in positions:
                pos_list[pos] = i
        paused_print_05(' '.join(pos_list), "\n")
        animation(word, pos_list, tries)
        if "_" not in pos_list:
            restart_question(name)
        else:
            return pos_list


def run_game(word, name):
    """
    Function that runs the main game: It calls functions to check the user input and
    compares it to the word in question.
    If the letter is in the word, the game progresses (more needs to be implemented)
    If the letter is not in the word, the try counter will be decreased.
    If all tries are used up, the player can choose to either start a new game
    or quit
    """
    tries = MAX_TRIES
    current_word = word
    pos_list = ['_' for x in range(len(word))]
    print(word)
    print(f"\nThe word has {len(word)} letters:\n")
    paused_print_1("_ "*len(word), "\n")
    print("You are at the start of your race,")
    print("try to get to the finish line!")
    animation(word, pos_list, tries)
    while tries > 0:
        x = guessed_letter_check()
        while True:
            if x in current_word:
                print_correct(x, word, pos_list, tries, name)
                break
            elif x not in current_word:
                paused_print_1(f"\nSorry, {x} is not part of the word.")
                print(f"Your current progress is:")
                print (' '.join(pos_list), "\n")
                tries -= 1
                animation(word, pos_list, tries)
                break
            elif ValueError:
                break
    else:
        paused_print_1("\nYou are out of fuel and lost!\n")
        paused_print_1(f"The word you were trying to guess was {word}\n")
        restart_question(name)

def animation(word, letter_list, tries):
    """
    This function prints out a "car race" where the amount of correctly 
    guessed letters will reduce the distance between car and finish,
    """
    start = len(guessed_letters)
    missing_letter = letter_list.count("_")-1
    while missing_letter > -1:
        pause(0.5)
        if start != 0:
            print("Your race progress:\n")
        elif start == 0:
            print(" ")
        print("\U0001F3C1", "_ "*missing_letter, "\U0001f697")
        while tries > 0:
            paused_print_05("Your fuel guage: ","\u2588 "*tries, "\n")
            if start != 0:
                print("All the letters you have guessed so far are:")
                print (' '.join(guessed_letters), "\n")
            paused_print_05("_" * 65)
            break
        break
    else:
        pause(0.5)
        paused_print_05("\U0001F697", "\U0001F3C1", "_\n")
        paused_print_1("Congratulations! You won the race!\n")
        
def main():
    """
    Main function that calls every function that is needed for the game.
    """
    global game_counter
    game_counter = 1
    name = take_user_name_input()
    print_rules(name)
    word = get_word()
    run_game(word, name)


if __name__ == "__main__":
    main()
