def twoSum (nums, target):
    pairs = []
    for i in range (len(nums)):
        for j in range (i + 1, (len(nums))):
            if nums[i] + nums [j] == target:
                pairs.append((i,j))
                
    return pairs
        
        
result = twoSum([1,2,3,2,4],5)
print (result)