'''
You are given an array of integers arr and a positive integer k. Your task is to find the maximum element in each sliding window of size k. The window slides from left to right, one element at a time, and you need to return the maximum element for each of these windows.
Input:
An integer array arr of size n, where 1≤n≤105
An integer k, where 1≤k≤n
Output:
An array of size n−k+1 containing the maximum element from each sliding window.
Examples:
Example 1
Input: arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
'''
def day23_sol(arr, k):
    l = []
    for i in range(len(arr)-k+1):
        l.append(max(arr[i:i+k]))
    return l

print(day23_sol([1, 3, -1, -3, 5, 3, 6, 7],3))
