"""
Make a list of numbers from a string just like in the previous problem. 
Make a new list with the cumulative sum of the numbers from the original string.

Sample Input:
12345

Sample Output:
[1, 3, 6, 10, 15]
"""

numbers = list(map(int, list(input())))
n = len(numbers)
result = [None] * n
for i in range(0, n):
    result[i] = sum(numbers[:i + 1])
print(result)
