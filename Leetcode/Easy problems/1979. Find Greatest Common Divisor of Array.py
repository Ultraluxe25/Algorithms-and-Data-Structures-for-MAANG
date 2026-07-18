"""
1979. Find Greatest Common Divisor of Array
Solved 18.07.2026
Easy
Topics: Array, Math, Number Theory

Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.


Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
Example 2:

Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.
Example 3:

Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.
 

Constraints:

2 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""

# Beats 100% time complexity, 96% space complexity (O(min(nums)) time complexity, O(1) space complexity)
class Solution:
    def findGCD(self, nums: list[int]) -> int:
        # Euclidean algorithm:
        # gcd(a, b) = gcd(b, a % b)
        # return math.gcd(smallest, biggest)
        
        smallest, biggest = min(nums), max(nums)
        
        div = smallest

        while div >= 1:
            if smallest % div == 0 and biggest % div == 0:
                return div

            div -= 1
