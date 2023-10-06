"""
343. Integer Break
Medium

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 
Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.


Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58
"""

# 1. If n is less than or equal to 3, it returns n - 1. This is because for values of n less than 4, 
# it's better to break it into smaller integers (e.g., 2 = 1 + 1) to maximize the product.

# 2. If n is divisible by 3, it tries to break it into as many 3s as possible, as this will maximize the product. 
# For example, for n = 6, it returns 3 * 3 = 9.

# 3. If n leaves a remainder of 1 when divided by 3, it breaks it into as many 3s as possible and leaves one 3 as 4. 
# For example, for n = 10, it returns 3 * 3 * 4 = 36.

# 4. If n leaves a remainder of 2 when divided by 3, it breaks it into as many 3s as possible and adds one more 3. 
# For example, for n = 8, it returns 3 * 3 * 2 = 18.

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        elif n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4
        elif n % 3 == 2:
            return 3 ** (n // 3) * 2
            