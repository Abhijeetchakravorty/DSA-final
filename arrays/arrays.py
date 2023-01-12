class Solution:
    def __init__(self):
        pass
    
    def twoSum(self, nums, target):
        numMap = dict()
        for i in range(len(nums)):
            complement = target - nums[i] # We calculate the complement
            if complement in numMap: # If we have the complement then
                return [numMap[complement], i] # we return the current index and the index of the complement present in numMap
            numMap[nums[i]] = i # We are storing the num in a dictionary

    
            
    

newHead = Solution()
nums = [3,2,4]
target = 6
print(newHead.twoSum(nums, target))

