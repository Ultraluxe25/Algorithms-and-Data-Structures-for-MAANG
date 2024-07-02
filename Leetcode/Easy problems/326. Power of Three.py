"""
326. Power of Three
Solved 02.07.2024
Easy
Topics: Math, Recursion

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 
Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33


Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
"""

# Solution 1 (Math)
from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        x = round(log(n, 3))
        print(x)

        return 3 ** x == n


# Solution 2 (Recursion)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        
        return self.isPowerOfThree(n / 3.0)
