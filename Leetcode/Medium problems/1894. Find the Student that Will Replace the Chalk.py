"""
1894. Find the Student that Will Replace the Chalk
Solved 02.09.2024
Medium
Topics: Array, Binary Search, Simulation, Prefix Sum

There are n students in a class numbered from 0 to n - 1. The teacher will give each student a problem starting with the student 
number 0, then the student number 1, and so on until the teacher reaches the student number n - 1. 
After that, the teacher will restart the process, starting with the student number 0 again.

You are given a 0-indexed integer array chalk and an integer k. There are initially k pieces of chalk. 
When the student number i is given a problem to solve, they will use chalk[i] pieces of chalk to solve that problem. 
However, if the current number of chalk pieces is strictly less than chalk[i], 
then the student number i will be asked to replace the chalk.

Return the index of the student that will replace the chalk pieces.


Example 1:

Input: chalk = [5,1,5], k = 22
Output: 0
Explanation: The students go in turns as follows:
- Student number 0 uses 5 chalk, so k = 17.
- Student number 1 uses 1 chalk, so k = 16.
- Student number 2 uses 5 chalk, so k = 11.
- Student number 0 uses 5 chalk, so k = 6.
- Student number 1 uses 1 chalk, so k = 5.
- Student number 2 uses 5 chalk, so k = 0.
Student number 0 does not have enough chalk, so they will have to replace it.


Example 2:

Input: chalk = [3,4,1,2], k = 25
Output: 1
Explanation: The students go in turns as follows:
- Student number 0 uses 3 chalk so k = 22.
- Student number 1 uses 4 chalk so k = 18.
- Student number 2 uses 1 chalk so k = 17.
- Student number 3 uses 2 chalk so k = 15.
- Student number 0 uses 3 chalk so k = 12.
- Student number 1 uses 4 chalk so k = 8.
- Student number 2 uses 1 chalk so k = 7.
- Student number 3 uses 2 chalk so k = 5.
- Student number 0 uses 3 chalk so k = 2.
Student number 1 does not have enough chalk, so they will have to replace it.
 

Constraints:

chalk.length == n
1 <= n <= 105
1 <= chalk[i] <= 105
1 <= k <= 109
"""

# Solution 1 (Brute Force)
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        result = 0
        round = 0
        n = len(chalk)

        total_chalk = sum(chalk)
        if k > total_chalk:
                k %= total_chalk

        while k > 0:
            result = round % n

            if chalk[result] > k:
                return round % n

            k -= chalk[result]
            print(k)
            round += 1

        return round % n
    

# Solution 2 (Short and effective)
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k %= total_chalk

        for i in range(len(chalk)):
            if chalk[i] > k:
                return i

            k -= chalk[i]
            