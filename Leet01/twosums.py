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

# for example (nums = [2, 7, 11, 15], target = 9)
# Step 1: index = 0, num = 2 complement = 9 - 2 = 7. 7 is not in the result. Insert as {2:0} in the result dict.
# Step 2: index = 1, num = 7 complement = 9 - 7 = 2. 2 is already in the result.The index for result[2] is 0.
# So we return the current index 1 and the index for result[2] is 0. 
# The answer is [0,1]
#The Space Complexity is also O(n) because, in the worst-case scenario 
# (e.g., the two matching numbers are at the very end of the array), the hash map will store up to n−1 elements.
