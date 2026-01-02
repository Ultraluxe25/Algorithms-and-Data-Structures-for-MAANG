"""
961. N-Repeated Element in Size 2N Array
Solved 02/01/2026
Easy
Topics: Array, Hash Table

You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.


Example 1:

Input: nums = [1,2,3,3]
Output: 3

Example 2:

Input: nums = [2,1,2,5,3,2]
Output: 2

Example 3:

Input: nums = [5,1,5,2,5,3,5,4]
Output: 5
 

Constraints:

2 <= n <= 5000
nums.length == 2 * n
0 <= nums[i] <= 104
nums contains n + 1 unique elements and one of them is repeated exactly n times.
"""

# Solution 1: Counter (O(n) time | O(n) space)
from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        freq = Counter(nums)
        mode = freq.most_common(1)

        return mode[0][0]
    

# Beats 100% Time | Beats 95.44% Space
# Solution 2: basic dict (O(n) time | O(1) space)
class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        freq = {}
        
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                return i
            