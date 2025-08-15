'''
Problem: Sort an Array of 0s, 1s, and 2s
You are given an array arr consisting only of 0s, 1s, and 2s.
The task is to sort the array in increasing order in linear time (i.e., O(n)) without using any extra space.
This means you need to rearrange the array in-place.

Input :
An integer array arr of size n where each element is either 0, 1, or 2.
Example : arr = [0, 1, 2, 1, 0, 2, 1, 0]

Output :
The sorted array, arranged in increasing order of 0s, 1s, and 2s.
Example: [0, 0, 0, 1, 1, 1, 2, 2]
'''

def day1_sol(arr):
    a = arr.count(0)
    b = arr.count(1)
    c = arr.count(2)
    arr = []
    arr.extend([0]*a)
    arr.extend([1]*b)
    arr.extend([2]*c)
    return arr

print(day1_sol([0, 1, 2, 1, 0, 2, 1, 0]))
