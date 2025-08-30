'''
You are given two integers, N and M. Your task is to find the Least Common Multiple (LCM) of these two numbers. The LCM of two integers is the smallest positive integer that is divisible by both N and M.
Input:
Two integers N and M, where 1≤N,M≤109
Output:
A single integer representing the Least Common Multiple of N and M.
Examples:
Example 1
Input: N = 4, M = 6
Output: 12
Explanation: The smallest number divisible by both 4 and 6 is 12.
'''
def day16_sol(n, m):
    if n % m == 0 or m % n == 0:
        return max(n, m)
    a, b = n, m
    while b != 0:
        a, b = b, a%b
    return n*m//a
    
print(day16_sol(4, 6))
