    # Variables that will help
    choice = ''
    hand = 0
    n = HAND_SIZE
 
    # Loop to keep it going:
    while choice != 'e':
   
        # Tell the user the choices and receive input
        choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
   
        # 'if' the user inputs n
        if choice == 'n':
 
            # Deal a new hand (start the game)
            hand = dealHand(n)
            playHand(hand.copy(),wordList,n)
 
        # 'elif' the user inputs r but no hand has been played
        elif choice =='r' and hand == 0:
 
            # Tell the user what must be done and a space afterwards
            print 'You have not played a hand yet. Please play a new hand first!'
            print ''
           
        # 'Elif' the user inputs r and hand is not 0
        elif choice == 'r' and hand != 0:
 
            # Play game with same hand as before
            playHand(hand,wordList,n)
 
        # 'elif' the user inputs e break out of the code
        elif choice == 'e':
            break
           
        # 'else' the user inputs anything else
        else:
            print 'Invalid command.'