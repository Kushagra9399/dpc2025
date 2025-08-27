'''
You are given a string s. Your task is to find and return the longest palindromic substring within the given string. A palindrome is a string that reads the same forwards and backwards.
Input:
A string s of length n. The length of the string satisfies 1≤n≤1000.
Output:
Return the longest substring of s that is a palindrome. If there are multiple solutions, return the first one that occurs.
Examples:
Example 1
Input: "babad"
Output: "bab"
Explanation: Both "bab" and "aba" are palindromic substrings, but since "bab" appears first in the string, it is returned.
'''
def day13_sol(s):
    def check(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l+1, r-1
    l, r = 0, 0
    for i in range(len(s)):
        l1, r1 = check(i, i)
        l2, r2 = check(i, i+1)
        if r1-l1 > r-l:
            l, r = l1, r1
        if r2-l2 > r-l:
            l, r = l2, r2
    return s[l:r+1]
    
print(day13_sol("babad"))
