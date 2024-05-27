"""
485. Max Consecutive Ones
Solved 27.05.2024
Easy

Hint
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. 
The maximum number of consecutive 1s is 3.


Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        repeat = 0

        for i in nums:
            if i == 1:
                repeat += 1
                if repeat > max_ones:
                    max_ones = repeat
            else:
                repeat = 0

        return max_ones
            