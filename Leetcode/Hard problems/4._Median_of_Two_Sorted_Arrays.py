"""
4. Median of Two Sorted Arrays
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
"""

# Solution 1 (Brute force)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numbers = sorted(nums1 + nums2)
        length = len(numbers)
        middle = length // 2

        if length % 2 == 0:
            result = sum(numbers[middle - 1: middle + 1]) / 2
        else:
            result = numbers[middle]

        return result
    

# Solution 2 (NumPy)
import numpy as np

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return np.median(nums1 + nums2)
    

# Solution 3 (Two pointers)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        i = 0  # Two pointers
        j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        result += nums1[i:]
        result += nums2[j:]
        
        n = len(result)
        if n % 2 == 1:
            return result[n // 2]
        else:
            return (result[n // 2 - 1] + result[n // 2]) / 2
    