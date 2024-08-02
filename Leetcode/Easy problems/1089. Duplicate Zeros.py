"""
1089. Duplicate Zeros
Solved 02.08.2024
Easy
Topics: Array, Two Pointers

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. 
Do the above modifications to the input array in place and do not return anything.


Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]


Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
"""

# Solution 1 (O(n) Space complexity)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        long = []
        for i in arr:
            long += [0, 0] if i == 0 else [i]
        print(long)            
        
        for i in range(len(arr)):
            arr[i] = long[i]


# Solution 2 (Many sub-arrays, O(n) space)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)  # 8 for Case 1
        
        while i < n - 1:
            if arr[i] == 0:
                sub = arr[i + 1 : n - 1]
                arr[i + 2 :] = sub
                arr[i + 1] = 0
                i += 2
            else:
                i += 1
                

# Solution 3 (O(n^2) Time complexity but O(1) space complexity)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)  # 8 for Case 1
        
        while i < n - 1:
            if arr[i] == 0:
                for j in range(n - 2, i, -1):
                    arr[j + 1] = arr[j]
                    
                arr[i + 1] = 0
                i += 2
            else:
                i += 1


# I guess that this task isn't easy level if we talk about O(n) for Time and O(1) for Space complexities.
