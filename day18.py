'''
Given a positive integer N, your task is to find the total number of divisors (factors) of N. A divisor of N is any integer that divides N without leaving a remainder.
A divisor of a number is any integer that divides the number evenly (i.e., without a remainder). For example, for N = 12, its divisors are 1, 2, 3, 4, 6, 12, so the total number of divisors is 6.
Input:
A single integer N, where 1≤N≤109
Output:
An integer representing the total number of divisors of N.
Examples:
Example 1
Input: N = 12
Output: 6
Explanation: The divisors of 12 are 1, 2, 3, 4, 6, and 12.
'''
import math
def day18_sol(n):
    divisors = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors += 1
    return divisors*2

print(day18_sol(12))
