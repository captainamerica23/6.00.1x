def hangman(secretWord):
    '''
  secretWord: string, the secret word to guess.
 
  Starts up an interactive game of Hangman.
 
  * At the start of the game, let the user know how many
    letters the secretWord contains.
 
  * Ask the user to supply one guess (i.e. letter) per round.
 
  * The user should receive feedback immediately after each guess
    about whether their guess appears in the computers word.
 
  * After each round, you should also display to the user the
    partially guessed word so far, as well as letters that the
    user has not yet guessed.
 
  Follows the other limitations detailed in the problem write-up.
  '''
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game, Hangman!"
    print "I am thninking of a word that is ", len(secretWord),"letters long."
    guessesleft=8
    lettersGuessed=''
    guess=''
   
    while (guessesleft>0 and not isWordGuessed(secretWord, lettersGuessed)):
        print "------------"
        print "You have ",guessesleft," guesses left."
        print "Available letters: ", getAvailableLetters(lettersGuessed)
        guess=raw_input('Please guess a letter: ')
        if(guess in lettersGuessed):
            print "Oops! You've already guessed that letter: ",getGuessedWord(secretWord, lettersGuessed)
        elif(guess in secretWord):
            lettersGuessed+=guess
            print "Good guess: ",getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed+=guess
            guessesleft-=1
            print "Oops! That letter is not in my word: ",getGuessedWord(secretWord, lettersGuessed)
    print "------------"
    if(isWordGuessed(secretWord, lettersGuessed)):
        print "Congratulations, you won!"
    else:
       print "Sorry, you ran out of guesses. The word was ",secretWord,"."