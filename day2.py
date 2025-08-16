'''
Problem: Find the missing number
You are given an array arr containing n-1 distinct integers. The array consists of integers taken from the range 1 to n, meaning one integer is missing from this sequence. Your task is to find the missing integer.

Input :
An integer array arr of size n-1 where the elements are distinct and taken from the range 1 to n.
Example : arr = [1, 2, 4, 5]

Output :
Return the missing integer from the array.
Example: Missing Number : 3
'''
def day2(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i]-1 != i:
            return i+1

print(day2([1,2,4,5]))
