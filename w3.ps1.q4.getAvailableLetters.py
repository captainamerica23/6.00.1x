def getAvailableLetters(lettersGuessed):
    '''
  lettersGuessed: list, what letters have been guessed so far
  returns: string, comprised of letters that represents what letters have not
    yet been guessed.
  '''
    # FILL IN YOUR CODE HERE...
    import string
    aLetters=''
    for tmp in string.ascii_lowercase:
        if tmp not in lettersGuessed:
            aLetters+=tmp
    return aLetters