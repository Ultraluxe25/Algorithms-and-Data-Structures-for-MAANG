"""
724. Find Pivot Index
Solved 09.07.2024
Easy
Topics: Array, Prefix sum

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11


Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.


Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
 

Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/
"""

# Solution 1 (Brute Force)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        elif sum(nums[1:]) == 0:
            return 0
        
        for i in range(1, n - 1):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i

        if sum(nums[:-1]) == 0:
            return n - 1

        return -1


# Solution 2 (O(n) beautiful solution)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)  # Left, right sums

        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
                
            left += nums[i]
            # print(left, right)

        return -1
        