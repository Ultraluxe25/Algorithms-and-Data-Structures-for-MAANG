"""
977. Squares of a Sorted Array
Solved 27.05.2024
Easy

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

 
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].


Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, 
could you find an O(n) solution using a different approach?
"""

# Solution 1 (Brute force)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_nums = list(map(lambda x: x * x, nums))
        square_nums.sort()
        
        return square_nums
        

# Solution 2 (Two pointers)
from math import pow

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [0 for i in range(len(nums))]
        # print(squared)
        i = 0  # Two pointers
        j = len(nums) - 1

        for k in range(len(nums) - 1, -1, -1):
            left = int(pow(nums[i], 2))
            right = int(pow(nums[j], 2))
            if right > left:
                squared[k] = right
                j -= 1
            else:
                squared[k] = left
                i += 1

        return squared
