


def CountOccurrencesEachNumber(num):
    
    Cnum = {}
    
    for number in num:
        if number in Cnum:
            Cnum[number] += 1
        else:
            Cnum[number] = 1
        
    return Cnum

results = CountOccurrencesEachNumber([1,2,2,3,3,3,3,4,1]) 
print (results)