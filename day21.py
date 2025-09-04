'''
You are given a stack of integers, and your task is to write a function that reverses the stack using recursion. You are not allowed to use any additional data structure (like arrays, lists, or another stack). The only operations you are allowed to perform are push, pop, and peek on the stack. The reversal must be done using recursion only.
Input:
A stack of integers. The stack may contain positive, negative, or zero values.
Output:
The stack should be reversed, meaning the element that was at the bottom of the original stack should become the topmost element after the reversal.
Examples:
Example 1
Input: [1, 2, 3, 4]
Output: [4, 3, 2, 1]
Explanation: 
Initially, the stack contains [1, 2, 3, 4].
After the reversal using recursion, the stack becomes [4, 3, 2, 1].
'''
def insert_ele(arr, ele):
    if not len(arr):
        arr.append(ele)
        return arr
    a = arr.pop()
    arr = insert_ele(arr, ele)
    arr.append(a)
    return arr

def day21_sol(arr):
    if not arr:
        return arr
    a = arr.pop()
    arr = day21_sol(arr)
    insert_ele(arr, a)
    return arr

print(day21_sol([1,2,3,4]))
