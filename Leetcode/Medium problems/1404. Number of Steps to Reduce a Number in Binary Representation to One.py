"""
1404. Number of Steps to Reduce a Number in Binary Representation to One
Solved 29.05.2024
Medium

Hint
Given the binary representation of an integer as a string s, 
return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

 
Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.


Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.


Example 3:

Input: s = "1"
Output: 0
 

Constraints:

1 <= s.length <= 500
s consists of characters '0' or '1'
s[0] == '1'
"""

class Solution:
    def numSteps(self, s: str) -> int:
        result = 0
        n = len(s)

        # s = sum([int(s[i]) * 2 ** (n - 1 - i) for i in range(n - 1, -1, -1)])
        
        total = 0
        for i in range(n):
            total += int(s[i]) * 2 ** (n - 1 - i)
        print(total)

        while total > 1:
            result += 1
            if total % 2 == 0:
                total //= 2
            else:
                total += 1

        return result

"""
```
🌟 Intuition

    🍀 I used a for loop to iterate through each element and multiply it by 2 with appropriate power.
    '1101' -> 1 * 2^3 + 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 8 + 4 + 0 + 1 = 13

🌟 Approach

    🍀 The 'result' will store number of actions to reduce decimal number to 1 and 'n' represents length of the binary number.

        result = 0 
        n = len(s)

    🍀 Next I used a for loop to iterate through each element of the 's' and multiply it by 2 with appropriate power.

        total = 0
        for i in range(n):
            total += int(s[i]) * 2 ** (n - 1 - i)
        print(total)

    🍀 You can get decimal representation from binary number using

        s = sum([int(s[i]) * 2 ** (n - 1 - i) for i in range(n - 1, -1, -1)])

        but it will cost You O(n) space complexity, so we have another way.

    🌴 Then I just used recomendations to the task:
        While total higher than 1:

    🌳 If the current number is even, you have to divide it by 2.
        if total % 2 == 0:

        🌿In this case we do total //= 2

    🌳 Else -> the current number is odd, you have to add 1 to it.

        🌿In this case we do total += 1

        So, here is last part of the code:

            while total > 1:
                result += 1
                if total % 2 == 0:
                    total //= 2
                else:
                    total += 1

            return result

🌟 Complexity
    🎯Time complexity: 0(n)
        0(2n) -> 0(n) (Two loops)

    🎯 Space complexity: 0(1)

😊 Thank You very much for Your attention and have a nice day 😉!
"""