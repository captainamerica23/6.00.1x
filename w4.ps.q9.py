    hand_choice = ''
    hand = ''
    while True:
        hand_choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if hand_choice == 'e':
            break
        elif hand_choice != 'n' and hand_choice != 'r':
            print "Invalid command."
            continue
        if hand_choice == 'n':
            hand = dealHand(HAND_SIZE)
        elif hand_choice == 'r':
            if hand == '': 
                print "You have not played a hand yet. Please play a new hand first!"+'\n'
                continue
        while True:
            player = raw_input('Enter u to have yourself play, c to have the computer play: ')
            if player != 'u' and player != 'c':
                print "Invalid command."
                continue
            if player == 'u':
                playHand(hand, wordList, HAND_SIZE)
            elif player == 'c':
                compPlayHand(hand, wordList, HAND_SIZE)
            break