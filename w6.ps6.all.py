import string
def buildCoder(shift):
    """
   Returns a dict that can apply a Caesar cipher to a letter.
   The cipher is defined by the shift value. Ignores non-letter characters
   like punctuation, numbers and spaces.
 
   shift: 0 <= int < 26
   returns: dict
   """
    coder = {}
    lshift = zip(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    ushift = zip(string.ascii_uppercase, string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift])
    return dict(lshift + ushift)
#------------
import string
 
def applyCoder(text, coder):
    """
   Applies the coder to the text. Returns the encoded text.
 
   text: string
   coder: dict with mappings of characters to shifted characters
   returns: text after mapping coder chars to original text
   """
    ### TODO
    ans=''
    for let in text:
       ans+=coder.get(let, let)
    return ans
#-----------------------
import string
 
def applyShift(text, shift):
    """
   Given a text, returns a new text Caesar shifted by the given shift
   offset. Lower case letters should remain lower case, upper case
   letters should remain upper case, and all other punctuation should
   stay as it is.
 
   text: string to apply the shift to
   shift: amount to shift the text (0 <= int < 26)
   returns: text after being shifted by specified amount.
   """
    ### TODO.
    ### HINT: This is a wrapper function.
   
    return applyCoder(text, buildCoder(shift))
 #----------------------------
import string
 
def findBestShift(wordList, text):
    """
   Finds a shift key that can decrypt the encoded text.
 
   text: string
   returns: 0 <= int < 26
   """
    ### TODO
    max_words = 0
    best_shift = 0
    lis = []
    for i in range(0,26):
        lis = applyShift(text, i).split(' ')
        count = 0
        for j in lis:
            if isWord(wordList, j):
                count += 1
        if count > max_words:
            max_words = count
            best_shift = i
 
    return best_shift
 
#-------------------------------
import string
 
def decryptStory():
    """
   Using the methods you created in this problem set,
   decrypt the story given by the function getStoryString().
   Use the functions getStoryString and loadWords to get the
   raw data you need.
 
   returns: string - story in plain text
   """
    wordList = loadWords()
    text= getStoryString()
 
    shift = findBestShift(wordList, text)
    return applyShift(text, shift)