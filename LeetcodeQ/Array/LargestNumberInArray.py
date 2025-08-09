#Find the Largest Number in an Array

def LargestNumberInArray ():
    
    maxNum = float('-inf')
    numList = [3,5,7,2,8]
    
    for i in range (len(numList)):
        if numList [i] > maxNum:
            maxNum = numList [i]
    
    return maxNum  
        
result = LargestNumberInArray() 
print(result )

    