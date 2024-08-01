"""
1496. Path Crossing
Solved 01.08.2024
Easy
Topics: Hash Table, String

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. 
You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. 
Return false otherwise.


Example 1:


Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.


Example 2:


Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
"""

# Solution (Hash Map via defaultdict)
from collections import defaultdict

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        X, Y = 0, 0
        steps = defaultdict(int)
        steps[(X, Y)] += 1  # Initial step

        for i in path:
            match i:
                case 'N':
                    Y += 1
                case 'W':
                    X -= 1
                case 'S':
                    Y -= 1
                case 'E':
                    X += 1
                case _:
                    return 'Wrong char in path!'
            
            if steps.get((X, Y)):
                return True

            steps[(X, Y)] += 1
            
        return False
