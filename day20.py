'''
Given a stack of integers, your task is to write a function that sorts the stack in ascending order. You are not allowed to use any additional data structure like arrays, lists, or another stack. The only operations you are allowed to perform are push, pop, and peek on the stack. The sorting must be performed using recursion only.
You need to recursively sort the stack, ensuring that after the sorting process, the stack remains sorted without using any additional data structures. You can only use the stack's own operations and recursion to solve this problem.
Input:
A stack containing integers. The stack may have positive, negative, or zero values.
Output:
The input stack should be sorted in ascending order (smallest elements on the top and largest at the bottom) after the sorting operation is performed.
Examples:
Example 1
Input: [3, 1, 4, 2]
Output: [1, 2, 3, 4]
Explanation: 
Initially, the stack contains [3, 1, 4, 2].
After sorting using recursion, the stack becomes [1, 2, 3, 4].
'''
def insert_ele(arr, ele):
    if not arr or arr[-1] <= ele:
        arr.append(ele)
        return arr
    a = arr.pop()
    arr = insert_ele(arr, ele)
    arr.append(a)
    return arr
    
def day20_sol(arr):
    if not arr or len(arr)==1:
        return arr
    a = arr.pop()
    arr = day20_sol(arr)
    arr = insert_ele(arr, a)
    return arr

print(day20_sol([3, 1, 4, 2]))
