"""
605. Can Place Flowers
Solved 05.07.2024
Easy

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true


Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

# O(n) space with While loop
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]  # Add empty borders
        j = 1
        while j < len(flowerbed) - 1:
            if sum(flowerbed[j-1:j+2]) < 1:
                flowerbed[j] = 1
                n -= 1
                j += 2
            else:
                j += 1

        return n <= 0


# O(n) space complexity with For loop
class Solution2:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Add empty plots at both ends to simplify edge cases
        flowerbed.insert(0, 0)
        flowerbed.append(0)

        for i in range(1, len(flowerbed) - 1):
            if not sum(flowerbed[i - 1 : i + 2]):
                # If the current plot and its neighbors are empty, plant a flower
                n -= 1
                flowerbed[i] = 1

        # If we've planted all required flowers (or more), return True
        return n <= 0
        

# O(1) space complexity
class Solution3:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_place = (i == 0) or flowerbed[i - 1] == 0
                right_place = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0

                if left_place and right_place:
                    flowerbed[i] = 1
                    n -= 1

        return n <= 0
        