'''
You are given an integer array coins[] of size n, where each element represents the denomination of a coin. You are also given an integer amount, representing the total amount of money. The task is to find the minimum number of coins required to make up the given amount.
If the amount cannot be formed by any combination of the coins, return -1.
You can assume that you have an infinite supply of each denomination.
Input:
An integer array coins[] where each element represents the value of a coin.
An integer amount representing the total amount of money
Output:
Return the minimum number of coins needed to make up the amount.
If the amount cannot be formed by any combination of coins, return -1.
Examples:
Example 1
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: To make the amount 11, the fewest number of coins is 3 (5 + 5 + 1).
'''
def day30_sol(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for j in coins:
            if i-j >= 0:
                dp[i] = min(dp[i], 1 + dp[i-j])
    return dp[-1] if dp[-1]!=float('inf') else -1

print(day30_sol([1,2,5],11))
