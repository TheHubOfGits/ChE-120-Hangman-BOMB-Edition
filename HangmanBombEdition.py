# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:05:21 2023

@author: alati
"""
import random
#AA and DF - Import random imports the random module, which includes a variety of functions associated with random number generation. 
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']
#AA and DF - The variable HANGMAN_PICS is defined as a set of 9 strings, each representing a different stage of the man hanging. The more incorrect guesses, the more limbs are added to the man. Only 8 wrong guesses are allowed.
words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango strawberry tomato'.split(),
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split(),
'MLB Teams':'angels astros braves cubs diamondbacks dodgers giants jays mariners marlins mets nationals orioles padres phillies rangers rays reds tigers yankees'.split(),
'NBA Teams':'bucks bulls cavaliers celtics clippers heat jazz knicks lakers magic mavericks nets nuggets pacers raptors spurs suns thunder timberwolves warriors'.split(),
'NHL Teams':'bruins flames blackhawks avalanche stars oilers kings wild canadiens devils islanders senators flyers penguins kraken lightning leafs knights capitals jets'.split(),
'NFL Teams':'bills cardinals bears vikings giants dolphins eagles buccaneers saints texans titans seahawks ravens steelers jaguars chiefs broncos chargers raiders colts'.split(),
'Countries':'italy russia poland germany brazil cameroon ethiopia azerbaijan kazakhstan australia liechtenstein rwanda canada netherlands myanmar argentina venezuela zimbabwe bangladesh'.split(),
'Capital Cities Around the World':'ottawa vienna rome berlin dublin kathmandu beijing santiago ankara athens baghdad budapest helsinki kabul madrid brasilia reykjavik'.split(),
'First Year Chem Eng Profs':'mahmoudi lucia aucoin tam kamkar hamilton mekonnen'.split(),}
#SP words is a dictionary that contains 4 sets, Colours, Shapes, Fruits, Animals. .split() then breaks the string whenever there is a space.

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    #NV: this line randomly chooses a list from the dictionary "words", being the categories, "colours", "fruits", "shapes", and "animals", and assigns this selected list to the variable "wordKey".

    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    #NV: this line selects a random integer from the ranges of 0, to 1 less than the length of the randomly selected list, "wordkey", and assigns it to the variable "wordIndex"

    return [wordDict[wordKey][wordIndex], wordKey]
    #NV: this line returns a list with the first entry being the item from the randomly selected list "wordKey" that corresponds to the index number from the randomly selected range specified in "wordIndex". The second entry is just the randomly selected list.

def displayBoard(missedLetters, correctLetters, secretWord):
    #AA - This function represents everything that is displayed to the user in the interface, including the variables missedLetters, correctLetters and secretWord.
    print(HANGMAN_PICS[len(missedLetters)])
    #AA - This print statement prints the Hangman picture from the list that is associated with the length of the missed letters variable. 
    #AA - Ex: print(HANGMAN_PICS(len(3))) would print HANGMAN_PICS[3]. 
    print()
    #AA - This print statement creates a empty line. No functionionality besides providing proper formatting. 
    
    print('Missed letters:', end=' ')
    #AA - This print statement prints the string Missed Letters: with an empty string on the end after the colon, which creates a space between the string Missed letters: and the first missed letter.  
    for letter in missedLetters:
        print(letter, end=' ')
        #AA - This for statement states that for a letter in the variable missedLetters(which is a list of strings), print letter with an empty string on the end, which creates a space between this letter and a potential next letter.  
    print()
    #AA - This print statement creates a empty line. No functionionality besides providing proper formatting. 

    blanks = '_' * len(secretWord)
    #AA - The variable blanks is displayed as a number of _ (underscores) equal to the number of letters in the secret word. 

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters: #DF - checks if any of the letters from secretWord are in correctLetters
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
        #SP replaces the _ with the correctly guessed letter from secretWord.

    for letter in blanks:
        print(letter, end=' ')
    print() #AA - This print statement creates a empty line. No functionionality besides providing proper formatting.  
    #SP prints out the letter separated by a space or underscore as the underscore represents an empty space

def getGuess(alreadyGuessed):
    while True:
    #SP starts an infinite loop that will keep asking the user for input until an acceptable input is given.
        print('Guess a letter.') #DF - Clue the player to guess a letter
        guess = input() #DF - Player inputs the guesses 
        guess = guess.lower()
        #SP takes the guess of the letter from the user and converts it into lowercase.
        if len(guess) != 1:
            print('Please enter a single letter.')
        #SP if the input is longer than 1 character it asks the user to input a single letter
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        #SP if the user guesses a letter they already guessed, it asks them to input a letter they haven't used already.
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        #SP if the user guesses anything that is not in the alphabet, it will ask the user to please enter a letter.
        else:
            return guess
        #SP and DF - if conditions are met, the guess is returned to go into the next process. 

def playAgain():
    #SP the function returns True if the user wishes to continue playing. If not it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
    #NV - if user inputs words starting with y, the game will play again. If anything else, the loop breaks. 

def selectBombLetter(secretWord):
    #AA = the function selects a random letter not in the secret word every game, and denotes it as the bomb letter.
    alphabet = 'abcdefghijklmnopqrstuvwxyz' #AA - list of the alphabet.
    while True:
        bomb = random.choice(alphabet) #AA - the bomb letter is a random letter from the alphabet every time. 
        if bomb not in secretWord:
            return bomb #AA - if the bomb letter chosen isn't in the secret word, return bomb. This makes it so that the bomb letter isn't a letter in the secret word.

def displayWarning():
    print ("Warning! There's a hidden 'bomb' letter in this game. Guess it and the game ends!") #message warning the player of the bomb letter hidden in the game.


print('H A N G M A N')
displayWarning()
#NV: prints the title of the game and well as warning the user about the bomb letter in the game. 

difficulty = ' '
while difficulty not in 'EMHI':
  print('Enter difficulty: E - Easy, M - Medium, H - Hard, I - Impossible')
  difficulty = input().upper()
#SP asks the user which difficulty they want by choosing E, M, H and converts the chosen letter to a capital so that there isn't an error.
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
#SP if they chose M it deletes the [7] and [8] hangman pictures which shortens the amount of 'lives' by 2.
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]
#SP if the H difficulty is chosen it deletes the [3] [5] [7] and [8] hangman pictures which shortens the amount of 'lives' by 4. 
if difficulty == 'I':
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[6]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]
    del HANGMAN_PICS[2]
    del HANGMAN_PICS[1]
#AA - if the I difficulty is chosen, the code deletes the [1] [2] [3] [5] [6] and [7] index's of the hangman pictures, which shortens the amount of 'lives' by 6.
#DF - if easy is chosen, the number of tries remains 8. 

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
bombLetter = selectBombLetter(secretWord)
gameIsDone = False
#SP and DF sets up the initial variables needed to start by randomizing them once more, or end the game depending on what the user chose. 

while True: #DF run if game is running
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)
#SP informs the user with the category of the word and displays the amount of characters and the corresponding image with the amount of guesses 
    guess = getGuess(missedLetters + correctLetters)
    #AA - this line means that inputting a letter that is already been guessed (either a part of missedLetters or correctLetters) will not be apart of the secret word. Essentially prevents user from wasting attempts by continuously inputting the same letter. Guess is a guess that hasn't already been guessed. 

    if guess == bombLetter:
        print('''Oh no! You guesses the bomb letter! Game Over!\n
         +---+
             |
        /|\  |
        / \  |
            ===''')
        gameIsDone = True #AA - if the player's guess is the bomb letter, they are informed that they guessed the bomb letter, the hangman picture without the head is printed, and the game ends. 
    elif guess in secretWord:
        correctLetters = correctLetters + guess
    #SP and DF takes user input and checks whether they have a correctly guessed letter or not. If guess is in the secret word, it is added to correctLetters. 
        foundAllLetters = True
    #NV foundAllLetters is set to True. 
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            #SP if all the indexs of secretWord are not in correctLetters, then the foundAllletters variable is now set to False instead of True, then the code breaks. The code than adds the users guess to missedLetters, and checks the next guess.
            #SP if all the indexs of secretWord are in correctLetters, then the rest of the nested statements aren't ran, and foundAllletters remains True. Since the user has guessed the correct word, the code prints that the user has won the game and gameisdone is set to True.
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
        #SP and DF if the user does get the word, it informs the user that they have won and returns that the game being done is True.
    else:
        missedLetters = missedLetters + guess
    #AA - adds the users incorrect guess to the list of missed letters. 

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
        #SP if the amount of missedLetters is equal to one less than the length of hangman pics, the user has guessed incorrectly too many times.
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            #NV: line above prints the following statement upon the game ending after running out of guesses...
            #You have run out of guesses!
            #After "number of missed guesses" missed guesses and "number of correct guesses" correct guesses, the word was "secretWord"
            gameIsDone = True
            #SP sets the gameisdone to True, ending the game.

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
            bombLetter = selectBombLetter(secretWord)
        #AA - If the game has finished and the player chooses to play again, the variables missedLetters and correctLetters are reset back to none, gameIsDone changes from true to false, the secret word and set which the word is selected from are randomized again so that another round may be played, and bombLetter is randomized again for a new letter not in the secret word. 
        else:
            break
        #AA - If the game has finished and the player chooses not to play again, the loop breaks.
