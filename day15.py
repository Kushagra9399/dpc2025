'''
You are given a string S, and your task is to find the length of the longest substring that contains no repeating characters. A substring is a contiguous block of characters in the string.
In this problem, you need to find the length of the longest substring where all the characters are unique. The substring can be formed by starting at any position in the string, but it must not contain any repeated characters.
Input:
A string S, where 1≤∣S∣≤105(length of string).
Output:
An integer representing the length of the longest substring without repeating characters.
Examples:
Example 1
Input: S = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with a length of 3. Even though the string contains repeated characters, the longest substring without duplicates is "abc".
'''
def day15_sol(s):
    d = {}
    max_len = 0
    last_repeat = 0
    for i in range(len(s)):
        if s[i] in d:
            if d[s[i]] < last_repeat:
                d[s[i]] = i
            else:
                max_len = max(max_len, i-last_repeat)
                last_repeat = d[s[i]]+1
                d[s[i]] = i
        else:
            d[s[i]] = i
    return max(max_len, i-last_repeat)
    
print(day15_sol("abcabcbb"))
