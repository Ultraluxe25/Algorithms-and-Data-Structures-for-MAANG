"""
2248. Intersection of Multiple Arrays
Solved 01.08.2024
Easy
Topics: Array, Hash Table, Sorting, Counting

Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, 
return the list of integers that are present in each array of nums sorted in ascending order.


Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].


Example 2:

Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation: 
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
 

Constraints:

1 <= nums.length <= 1000
1 <= sum(nums[i].length) <= 1000
1 <= nums[i][j] <= 1000
All the values of nums[i] are unique.
"""

# Solution 1 (using Hash Table)
from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = []
        n = len(nums)
        common = defaultdict(int)

        for lst in nums:
            for i in lst:
                common[i] += 1

        # print(common)
        for key, value in common.items():
            # print(key, value, n)
            if value == n:
                result.append(key)

        return sorted(result)


# Solution 1 (using Hash Set)
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common = set(nums[0])
        for i in nums[1:]:
            common &= set(i)

        return sorted(common)
    