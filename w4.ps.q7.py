    bestScore = 0

    bestWord = None

    for word in wordList:

        if isValidWord(word, hand, wordList):

            score = getWordScore(word, n)

            if score > bestScore:

                bestScore = score
                bestWord = word

    return bestWord