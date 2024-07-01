/*
1550. Three Consecutive Odds
Solved 01.07.2024
Easy
Topics: Array

Hint
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.


Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
*/

#include <stdbool.h>

bool threeConsecutiveOdds(int* arr, int arrSize) {
    for (int i; i < arrSize - 2; i++) {
        int multiplication = arr[i] * arr[i + 1] * arr[i + 2];
        if (multiplication % 2 == 1) {
            return true;
        }
    }
    return false;    
}
