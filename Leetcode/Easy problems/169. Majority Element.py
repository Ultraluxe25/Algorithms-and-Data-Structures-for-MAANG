"""
169. Majority Element
Solved 07.06.2024
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

 
Example 1:

Input: nums = [3,2,3]
Output: 3


Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

# Solution 1 (Brute Force)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in set(nums):
            if nums.count(i) > n / 2:
                return i
        

# Solution 2 (O(nlogn))
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        middle = nums[len(nums) // 2]  # Most frequent element stores element in the middle of the array
        return middle
        