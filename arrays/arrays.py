class Solution:
    def __init__(self):
        pass
    
    def maxConsecutiveOnes(self, arr):
        count = 0
        result = 0
        for i in range(len(arr)):
            if(arr[i]==1):
                count += 1
            else:
                result = max(count, result)
                count = 0
        result = max(result, count)
        return result
    
    def findEvenNumbers(self, arr):
        count = 0
        for i in range(len(arr)):
            if(len(str(arr[i]))%2==0):
                count += 1
        return count
    
    def squareSortedArr(self, nums):
        arr = sorted([i*i for i in nums])
        return arr
    
    # def duplicateZeroes(self, nums):
        
    
    
    
    # Two sum
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

