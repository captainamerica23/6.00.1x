    i=0
    newhand={}
    keyshand = hand.keys()
    valueshand=hand.values()
 
    for char in keyshand:
        newhand[char]=valueshand[i]
        i+=1
 
 
    for char in word:      
        #print char
        if char in hand.keys():
            newhand[char]=newhand[char]-1
        else:
            newhand[char]=newhand[char]
    #print hand
    return newhand