#W4 Problem Set Question 1
    points=0
    for char in word:
        #print char
        #print 'individual',SCRABBLE_LETTER_VALUES[char]
        x=SCRABBLE_LETTER_VALUES[char]
        points=points+x
        #print 'sum',points
 
    point=points*len(word)
    #print pointt
 
    if n==len(word):
        return point+50
    else:
        return point