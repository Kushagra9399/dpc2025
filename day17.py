'''
Given a positive integer N, your task is to find its prime factorization. Return a list of prime numbers that multiply together to give N. If N is prime, the output should be a list containing only N.
Prime factorization is the process of breaking down a number into the set of prime numbers that, when multiplied together, result in the original number. For example, if N = 18, its prime factors are [2, 3, 3] because 2×3×3=18.
Input:
A single integer N, where 2≤N≤109
Output:
A list of prime numbers representing the prime factorization of N.
Examples:
Example 1
Input: N = 18
Output: [2, 3, 3]
Explanation: The prime factorization of 18 is 2 × 3 × 3.
'''
def day17_sol(n):
    prime_factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            prime_factors.append(i)
            n = n//i
        else:
            i += 1
    return prime_factors

print(day17_sol(18))
