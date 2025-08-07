
def MaximumProductTwoNumbers(nums):
    maxTwoNum = []
    maxProduct = float('-inf')
    
    for i in range (len(nums)):
        for j in range (i + 1, len(nums)):
            product = nums[i] * nums[j]
            if product > maxProduct:
                maxProduct = product
                maxTwoNum = [nums[i], nums[j]]
    
    return maxProduct
    
    
    
    
results= MaximumProductTwoNumbers([5,3,2,6,1])
print(results)