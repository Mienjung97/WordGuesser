import random
import time
import re
from words import word_list, MAX_TRIES

guessed_letters = []
game_counter = 1


def print_ascii(i):
    """
    This function is used to print different ASCII arts. (Function cannot 
    be collapsed because indentation will move the )
    """
    if i == 0:
        print(r"""   
 _       __                  __ ______                                    
| |     / /____   _____ ____/ // ____/__  __ ___   _____ _____ ___   _____
| | /| / // __ \ / ___// __  // / __ / / / // _ \ / ___// ___// _ \ / ___/
| |/ |/ // /_/ // /   / /_/ // /_/ // /_/ //  __/(__  )(__  )/  __// /    
|__/|__/ \____//_/    \__,_/ \____/ \__,_/ \___//____//____/ \___//_/     
                                                                                                                                                
        """)
    elif i == 1:
        paused_print_1(r"""
    
   ___                    __          __   __         ___ _        _       __ 
  / _ \ ___ _ ____ ___   / /_ ___    / /_ / /  ___   / _/(_)___   (_)___  / / 
 / , _// _ `// __// -_) / __// _ \  / __// _ \/ -_) / _// // _ \ / /(_-< / _ \
/_/|_| \_,_/ \__/ \__/  \__/ \___/  \__//_//_/\__/ /_/ /_//_//_//_//___//_//_/
   __        ___                                         ___            __    
  / /  ___  / _/___   ____ ___   __ __ ___  __ __ ____  / _/__ __ ___  / /    
 / _ \/ -_)/ _// _ \ / __// -_) / // // _ \/ // // __/ / _// // // -_)/ /     
/_.__/\__//_/  \___//_/   \__/  \_, / \___/\_,_//_/   /_/  \_,_/ \__//_/      
                               /___/ __   __                                  
  ____ __ __ ___   ___   ___  __ __ / /_ / /                                  
 / __// // // _ \ (_-<  / _ \/ // // __//_/                                   
/_/   \_,_//_//_//___/  \___/\_,_/ \__/(_)                                    
                                                                              
    """)
    elif i == 2:
        print(r"""
   ______                                   __         __
  / ____/____   ____   ____ _ _____ ____ _ / /_ _____ / /
 / /    / __ \ / __ \ / __ `// ___// __ `// __// ___// / 
/ /___ / /_/ // / / // /_/ // /   / /_/ // /_ (__  )/_/  
\____/ \____//_/ /_/ \__, //_/    \__,_/ \__//____/(_)   
__  __              /____/                               
\ \/ /____   __  __   _      __ ____   ____              
 \  // __ \ / / / /  | | /| / // __ \ / __ \             
 / // /_/ // /_/ /   | |/ |/ // /_/ // / / /             
/_/ \____/ \__,_/    |__/|__/ \____//_/ /_/              
   __   __                                      __       
  / /_ / /_   ___     _____ ____ _ _____ ___   / /       
 / __// __ \ / _ \   / ___// __ `// ___// _ \ / /        
/ /_ / / / //  __/  / /   / /_/ // /__ /  __//_/         
\__//_/ /_/ \___/  /_/    \__,_/ \___/ \___/(_)          
                                                                                                                                                       
""")
    elif i == 3:
        print(r"""
    ______                   __            __                 __    __
   / ____/____ ___   ____   / /_ __  __   / /_ ____ _ ____   / /__ / /
  / __/  / __ `__ \ / __ \ / __// / / /  / __// __ `// __ \ / //_// / 
 / /___ / / / / / // /_/ // /_ / /_/ /  / /_ / /_/ // / / // ,<  /_/  
/_____//_/ /_/ /_// .___/ \__/ \__, /   \__/ \__,_//_/ /_//_/|_|(_)   
                 /_/          /____/                                  
        """)

def print_line():
    """
    Add 79 dashes to form a line
    """
    print("_"*79, "\n")

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
        if len(name) > 0:
            break
        else:
            print("You must enter a name.")
            return take_user_name_input()
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
    paused_print_2("in your racear to try and finish the race.\n")
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
    input("Press the Enter key to start!\n")

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
        print(f"{name}, this is your Game no. {game_counter}! Have fun!")
        guessed_letters.clear()
        new_word = get_word()
        run_game(new_word, name)
    elif y.lower() == "n":
        print(f"\nThank you for playing the game, {name}!")
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
    the alphabet and no letters or signs. Letters will always be converted
    into lower case for validation.
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
        # Regular expressions (re) are used to find double occuring letters.
        positions = [m.start() for m in re.finditer(i, word)]
        for pos in positions:
                pos_list[pos] = i
        # Following statement will print the word including "_" for unguessed letters.
        paused_print_05(' '.join(pos_list))
        animation(word, pos_list, tries)
        if "_" not in pos_list:
            restart_question(name)
        else:
            return pos_list

def run_game(word, name):
    """
    Function that runs the main game: It calls functions to check the user input and
    compares it to the word in question.
    The game passes the guess into the "guessed_letter_check" function which will return 
    the letter if it was a valid input.
    If the guess was correct, the "print_correct" function is called.
    If the letter is not in the word, the try counter will be decreased and the fail will
    be passed into the "animation" function to reduce the "fuel" (trys).
    If all tries are used up, the player can choose to either start a new game
    or quit
    """
    print_ascii(1)
    tries = MAX_TRIES
    current_word = word
    pos_list = ['_' for x in range(len(word))]
    print(word)
    print(f"\nThe word has {len(word)} letters:\n")
    paused_print_1("_ "*len(word))
    print("\nYou are at the start of your race,")
    print("try to get to the finish line!")
    animation(word, pos_list, tries)
    while tries > 0:
        x = guessed_letter_check()
        while True:
            if x in current_word:
                print_correct(x, word, pos_list, tries, name)
                break
            elif x not in current_word:
                paused_print_1(f"\nSorry, {x} is not part of the word.\n")
                print(f"Your current progress is:")
                print (' '.join(pos_list), "\n")
                tries -= 1
                animation(word, pos_list, tries)
                break
            elif ValueError:
                break
    else:
        print_ascii(3)
        paused_print_1("\nYou are out of fuel and lost!\n")
        paused_print_1(f'The word you were trying to guess was "{word}"\n')
        restart_question(name)

def animation(word, letter_list, tries):
    """
    This function prints out a "car race" where the amount of correctly 
    guessed letters will reduce the distance between car and finish.
    It also prints out the remaining trys in form of "fuel bars" as well
    as all the previously guessed letters.
    """
    start = len(guessed_letters)
    missing_letter = letter_list.count("_")-1
    while missing_letter > -1:
        pause(0.5)
        if start != 0:
            print("\nYour race progress:")
        elif start == 0:
            print(" ")
        # The unicode numbers represent "Finish flag", "red car" and the "fuel bars".
        print("\U0001F3C1", "_ "*missing_letter, "\U0001f697")
        while tries > 0:
            print("Your fuel guage: ","\u2588 "*tries)
            if start != 0:
                pause(1)
                print("\nAll the letters you have guessed so far are:")
                print (' '.join(guessed_letters), "\n")
            paused_print_05("_" * 79)
            break
        break
    else:
        # This is the output for winning the "race".
        paused_print_05("\n")
        print("\U0001F697", "\U0001F3C1", "_\n")
        print_ascii(2)
        pause(1)
        
def main():
    """
    Main function that calls every function that is needed for the game.
    """
    global game_counter
    game_counter = 1
    print_ascii(0)
    name = take_user_name_input()
    print_rules(name)
    word = get_word()
    run_game(word, name)

if __name__ == "__main__":
    main()
