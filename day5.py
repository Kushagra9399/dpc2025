'''
Problem : Find the Leaders in an Array
You are given an integer array arr of size n.
An element is considered a leader if it is greater than all the elements to its right.
Your task is to find all such leader elements in the array.

Input :
An integer array arr of size n.
Example : 
arr = [16, 17, 4, 3, 5, 2]

Output :
Return an array containing all the leader elements in the order in which they appear in the original array.
Example:
Leaders: [17, 5, 2]
'''

def day5(arr):
    a = []
    curr_max = -1
    for i in range(len(arr)-1,-1,-1):
        if arr[i] > curr_max:
            a.append(arr[i])
            curr_max = arr[i]
    return a[::-1]

print(day5([16, 17, 4, 3, 5, 2]))
