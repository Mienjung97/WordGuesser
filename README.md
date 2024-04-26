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
