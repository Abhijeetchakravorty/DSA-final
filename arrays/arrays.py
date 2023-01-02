class Solution:
    def __init__(self):
        pass
    
    def twoSum(self, nums, target):
        numMap = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
#Approach
#Start by setting a number and its index
#Iterate over the array by using that index and its vakue
#In case currnt num+previously set index == target then return the indexes
#In casse not then increment the index
        
            
                
    

    
            
    

newHead = Solution()
nums = [3,2,4]
target = 6
print(newHead.twoSum(nums, target))

