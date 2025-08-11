

def secondLargestNumber(nums):
    largest = float('-inf')
    secLargest = float('-inf')
    num = [0,5,20,8,15]
    
    for num in nums: 
        if num > largest:
                secLargest = largest 
                largest = num
        
        elif num > secLargest and num != largest:
            secLargest = num 
            
   
    return secLargest
    
    
    
    
    
    
result = secondLargestNumber([0,5,20,8,15])
print(result)


