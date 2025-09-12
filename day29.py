'''
You are given an integer n. Your task is to calculate the n-th Fibonacci number using Dynamic Programming.
The Fibonacci sequence is a series of numbers where:
F(0)=0
F(1)=1
For n≥2, F(n)=F(n−1)+F(n−2)
Your task is to compute F(n) efficiently by using a bottom-up dynamic programming approach, avoiding redundant calculations.
Input:
A single integer n (0 ≤ n ≤ 1000).
Output:
Return the n-th Fibonacci number.
Examples:
Example 1
Input: 5
Output: 5
Explanation: The 5th Fibonacci number is 5. The sequence up to F(5) is [0, 1, 1, 2, 3, 5].
'''
def day29_sol(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

print(day29_sol(5))
