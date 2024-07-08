"""
1464. Maximum Product of Two Elements in an Array
Solved 08.07.2024
Easy
Topics: Array, Sorting, Heap (Priority Queue)

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 


Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12
 

Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3
"""

# Solution 1 (Sorting)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-2] - 1) * (nums[-1] - 1)
        

# Solution 2 (Best)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = 0
        second = 0
        
        for i in nums:
            if i > first:
                second = first
                first = i
            else:  # first >= i >= second
                second = max(second, i)

        return (first - 1) * (second - 1)
        