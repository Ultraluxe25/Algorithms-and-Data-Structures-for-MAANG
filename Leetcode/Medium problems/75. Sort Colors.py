"""
75. Sort Colors
Solved 12.06.2024
Medium
Topics: Array, Two Pointers, Sorting

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color 
are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 
Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

# Solution 1 (Original idea's solution)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch national flag problem
        # https://en.wikipedia.org/wiki/Dutch_national_flag_problem

        red, white, blue = 0, 0, len(nums) - 1  # Three pointers
        while white <= blue:
            if nums[white] == 0:  # Red color
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif nums[white] == 1:  # White color
                white += 1
            elif nums[white] == 2:  # Blue color
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1     


# Solution 2 (Bubble sort)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    