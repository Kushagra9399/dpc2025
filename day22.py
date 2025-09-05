'''
You are given an array of integers and an integer k. Your task is to find the first element in the array that appears exactly k times. If no such element exists, return -1.
Input:
An integer array arr of size n, where 1≤n≤105
An integer k, where 1≤k≤n
Output:
Return the first element from the array that occurs exactly k times. If no element occurs exactly k times, return -1.
Examples:
Example 1
Input: arr = [3, 1, 4, 4, 5, 2, 6, 1, 4], k = 2
Output: 1
Explanation: 
Element 1 appears twice in the array (at index 1 and index 7), making it the first element that appears exactly 2 times.
'''
def day22_sol(arr, k):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 0
        d[i] += 1
    for i in arr:
        if d[i] == k:
            return i
    return -1
    
print(day22_sol([3, 1, 4, 4, 5, 2, 6, 1, 4], 2))
