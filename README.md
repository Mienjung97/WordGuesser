# WordGuesser
Word Guesser is a game that bases its core functionality on the well known game "Hangman" - but this version lets you race against the fuel in your racecar.

The game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku in which you are trying to guess a car brand, which is randomly choosen for each try.

Click [here](https://wordguesserrace-cdad6feac143.herokuapp.com/) to get to the live version of [WordGuesser](https://wordguesserrace-cdad6feac143.herokuapp.com/).

![WordGuesser](readme/responsiveness.PNG)

## How to play

WordGuesser is based on the game hangman, on which you can read more about on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)).

First, the game asks you to put in a name, after which the user will be presented with the rules. To start the game, the user has to press the "enter" key and is then in a game loop, in which the game can be played as often as the user wants to.

As soon as the game starts, the amount of letters in the word will be displayed as well as underscores representing the missing letters. Additionally, the game will print a car, finish flag and a distance (underscores) between them.

Instead of just being punished for wrong inputs, the player will be rewarded for correct guesses by moving the racecar closer to the finish line. The "punishment" for guessed letters that are not contained in the word to guess, the player will loose one bar of fuel. 

The words to guess are all car brands, ranging from three up to 12 letters. To make the game easier, any letter will be lower case and there are no whitespaces or dashes in the names. The player starts with 6 fuel bars (tries).

After the game is finished, either by winning or loosing, the user will be asked to replay or end the game.

## Features

- The list of words contains 48 different car brands, which are choosen via the "random" module. This list was generated with ChatGPT and modified by me.
- For an easier game, Chinese and Russian car brands were excluded.

![list](readme/ChatGPT_list.PNG)

- The username input will allow any character and a length between 1 and 23, and after confirming, the game greets the user.

![login](readme/username_input.PNG)

- The terminal will clear and provide the user with the games rules, which are printed out with a time delay.
- The rules are too long for the single page, so the terminal will scroll.

![rules-msg](readme/rules_top.PNG)
![rules](readme/rules.PNG)

- After confirming with the "enter" key, the terminal will clear an show the following message:

![start-game](readme/start_msg.PNG)

- This message will be cleared after 5 seconds, then the user will be shown the first "real" game page:

![main-game](readme/main_game.PNG)

- After each guess, the terminal will be cleared and shows the user if the letter was correct or false, as well as every previously guessed letter, the race progress and the fuel guage.

- Almost every print statement has an artificial pause between 0.5 and 5 seconds added.

Wrong input
(only 5 fuel bars remain in this picture):

![wrong](readme/wrong_letter.PNG)

Correct input (the car gets a bit closer to the finish):

![corret](readme/correct_msg.PNG)

- Every input will be validated and only single letters that have not been guessed will be returned. If the user enters numbers, special symbols or multiple characters, the game will display a corresponding error message and ask again for a new input. 

- If the input was invalid, the terminal will not be cleared so that the user is able to scroll back up and see the current progress.

![validation-letter](readme/validation_msg.PNG)

- If the game is won, the user will be shown that the car has crossed the finish line, some ASCII art will congratulate and the user will be asked if the game should end or restart:

![won-game](readme/won_game.PNG)

- If the user looses, the progress before loosing, as well as a different ASCII art will be shown, and a message informing about the loss and the brand to guess:

![lost-game](readme/lost_game.PNG)

- The restart question also has validation and only accepts "y" and "n", both in lower and upper case. Any other input will print a corresponding message and ask for another input:

![end-game-validation](readme/end_game_validation.PNG)

- If the user selects a new game, it starts of with showing the game counter and the original start ASCII art:

![restart-game](readme/game_counter.PNG)

- If the user decides to end the game, a "Thank you" ASCII art will be shown:

![end-game](readme/end_game_msg.PNG)

## Data Model

The game does not have any classes and relies just on functions and one global variable. 

For better readability, I moved small functions, like "paused_print" (delayed print) and clearing the terminal into the "helper.py" file. 

The list of words as well as the global constant (game counter) are in the "words.py" file.

The function to print out different ASCII arts is in the file "art.py".

Besides the files and functions that I have created, the game also imports the following modules:

- os
- time
- random
- re

##