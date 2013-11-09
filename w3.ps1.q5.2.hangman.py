def hangman(secretWord):
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long'
    print '-----------'
    secretWord = secretWord
    lettersGuessed = []
    mistakesMade = 8
 
    while mistakesMade > 0:
        availableLetters = getAvailableLetters(lettersGuessed)
        print 'You have ' + str(mistakesMade) + ' guesses left'
        print 'Available Letters: ' + availableLetters
        userGuess = raw_input('Please guess a letter: ')
        userGuess = userGuess.lower()
        if userGuess in availableLetters:
            lettersGuessed += [userGuess,]
            if userGuess in secretWord:
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
                    print '-----------'
                    return 'Congratulations, you won!'
                else:
                    print 'Good Guess: ' + getGuessedWord(secretWord, lettersGuessed)
            else:
                print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
                mistakesMade -= 1
        else:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
        print '-----------'  
    print 'Sorry, you ran out of guesses. The word was ' + secretWord