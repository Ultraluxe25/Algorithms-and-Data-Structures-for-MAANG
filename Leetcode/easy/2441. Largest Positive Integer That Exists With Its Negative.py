"""
2441. Largest Positive Integer That Exists With Its Negative
Solved 02.05.2024
Easy

Hint
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
Return the positive integer k. If there is no such integer, return -1.

 
Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.


Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.


Example 3:

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.
 

Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
nums[i] != 0
"""

# Solution 1 (set of unique)
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)  # Removes duplicates
        intermediate = -1
        for number in nums:
            if -number in nums and abs(number) > intermediate:
                intermediate = abs(number)

        return intermediate
    

# Solution 2 (descending sort)
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        k = -1
        nums.sort(reverse=True)
        for i in nums:
            if i > 0 and -i in nums:
                return i
        
        return k
    

# Solution 3 (two pointers)
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        k = -1
        nums.sort()
        left = 0  # First and last indexes
        right = len(nums) - 1

        while left < right:
            if -nums[left] == nums[right]:
                return nums[right]
            elif nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1
        
        return k
