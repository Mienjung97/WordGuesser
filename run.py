import random
import time
import re
from words import word_list

guessed_letters = []

def pause(u):
    """
    Function to delay print statements adn takes a float as delay
    in seconds.
    """
    time.sleep(u)

def log_in():
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
        return log_in()
            
    print("-"*23)
    print(f"\nHello {name} and welcome to WordGuesser\n")
    pause(1)
    return name

def print_rules(name):
    """
    Function that prints the rules and game explanation.
    """
    print("-"*65, "\n")
    print("WordGuesser is a game like Hangman, just less cruel:")
    print("Instead of hanging a man, you will race against the fuel")
    print("in your racear to try and finish the race.\n")
    pause(2)
    print("The game works as following:\n")
    pause(0.5)
    print("1. You need to try and guess the word, letter by letter.\n")
    pause(0.5)
    print("2. With each try, you will put in a single letter ")
    print("   that you think is contained in the word.\n")
    pause(0.5)
    print("3. If the letter you provided is contained in the word,")
    print("   the game is going to show you in which position it is")
    print("   and your racecar moves forward.\n")
    pause(0.5)
    print("4. If the word does not contain the letter, your try ")
    print("   counts as a fail and reduces the fuel that you have left.\n")
    pause(0.5)
    print("5. You only have 6 tries, or you loose the game.\n")
    pause(0.5)
    print(f"6. Have fun, {name}, and try to win as many races as possible!\n")
    print("-"*65, "\n")
    pause(1)

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
    y = input(f"{name}, would you like to restart the game? (Y/N)\n")
    if y.lower() == "y":
        # game_counter += 1 -> I wanted to include a game counter, but it always just counts to 2
        # I tried global, inside and outside of the if statement
        print("\n")
        print("-"*65, "\n")
        print(f"{name}, this is your x game! Have fun!") #{game_counter}
        guessed_letters.clear()
        new_word = get_word()
        run_game(new_word, name)
    elif y.lower() == "n":
        print(f"Thank you for playing the game, {name}!")
        exit()
    else:
        print("Please enter a valid input.")
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
            print("Please enter only letters, no numbers.")
            return guessed_letter_check()
    elif len(i) != 1:
        print("Please enter only one letter.")
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
        print (' '.join(pos_list), "\n")
        pause(0.5)
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
    tries = 6
    current_word = word
    pos_list = ['_' for x in range(len(word))]
    print(word)
    print(f"\nThe word has {len(word)} letters:\n")
    print("_ "*len(word), "\n")
    pause(1)
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
                print(f"\nSorry, {x} is not part of the word.")
                pause(1)
                print(f"Your current progress is:")
                print (' '.join(pos_list), "\n")
                tries -= 1
                animation(word, pos_list, tries)
                break
            elif ValueError:
                break
    else:
        print("\nYou are out of fuel and lost!\n")
        pause(1)
        print(f"The word you were trying to guess was {word}\n")
        pause(1)
        restart_question(name)


def animation(word, letter_list, tries):
    """
    This function prints out a "car race" where the amount of correctly 
    guessed letters will reduce the distance between car and finish,
    """
    missing_letter = letter_list.count("_")-1
    while missing_letter > -1:
        pause(0.5)
        print("Your race progress:\n")
        print("\U0001F3C1", "_ "*missing_letter, "\U0001f697")
        while tries > 0:
            print("Your fuel guage: ","\u2588 "*tries, "\n")
            pause(0.5)
            print("All the letters you have guessed so far are:")
            print (' '.join(guessed_letters), "\n")
            print("_"*65)
            pause(0.5)
            break
        break
    else:
        pause(0.5)
        print("\U0001F697", "\u0126", "_\n")
        pause(0.5)
        print("Congratulations! You won the race!\n")
        

def main():
    """
    Main function that calls every function that is needed for the game.
    """
    name = log_in()
    print_rules(name)
    word = get_word()
    run_game(word, name)

if __name__ == "__main__":
    main()
