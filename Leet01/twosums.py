# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums:list[int],target : int)-> list[int]:
        result = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in result:
                return [result[complement], index]
            result[num] = index
        return []
# testcases
print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
    
