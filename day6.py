'''
Problem : Find All Subarrays with Zero Sum
You are given an integer array arr of size n. Your task is to find all the subarrays whose elements sum up to zero. A subarray is defined as a contiguous part of the array, and you must return the starting and ending indices of each subarray.

Input :
An integer array arr of size n where n represents the number of elements in the array.
Example : 
Input: [1, 2, -3, 3, -1, 2]

Output :
- Return a list of tuples, where each tuple contains two integers. The starting index (0-based) of the subarray. The ending index (0-based) of the subarray.
- The output should list all subarrays that sum to zero. If no such subarrays are found, return an empty list.
Example
Output: [(0, 2), (2, 3)]
'''

def day6_sol(arr):
    l = []
    sums = {0 : [-1]}
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum in sums:
            for j in sums[curr_sum]:
                l.append((j+1,i))
            sums[curr_sum].append(i)
        else:
            sums[curr_sum] = [i]
    return l

print(day6_sol([-3, 1, 2, -3, 4, 0]))
