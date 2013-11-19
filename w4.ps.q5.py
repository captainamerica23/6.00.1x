    # Keep track of two numbers: the number of letters left in your hand and the total score
    score=0
    uhand=hand.copy()
       
    # As long as there are still letters left in the hand:
    while calculateHandlen(uhand)>0:
        # Display the hand
        print 'Current hand: ',
        print (displayHand(uhand))
        # Ask user for input
        word=raw_input ('Enter word, or a "." to indicate that you are finished: ')
       
        # If the input is a single period:
        if word == '.':
                   
            # End the game (break out of the loop)
            break
           
        # Otherwise (the input is not a single period):
        else:
                   
            # If the word is not valid:
            if isValidWord(word, uhand, wordList) == False:
           
                # Reject invalid word (print a message followed by a blank line)
                print ('Invalid word, please try again.')
                print
 
            # Otherwise (the word is valid):
            else:
               
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score+=getWordScore(word, n)
                print ('"'+str(word) + '" earned '+str(getWordScore(word, n))+' points. Total: ' + str(score) + ' points.')
                print
                # Update the hand
                uhand=updateHand(uhand, word)
               
 
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(uhand)>0:
        print ('Goodbye! Total score: ' + str(score)+ ' points.')
    else:
        print ('Run out of letters. Total score: ' + str(score)+ ' points.')