'''
You are given a string s of lowercase English alphabets and an integer k. Your task is to count all possible substrings of s that contain exactly k distinct characters.
Input:
A string s consisting of lowercase English letters.
An integer k, where 1 ≤ 𝑘 ≤ 26
The length of the string satisfies 1 ≤ 𝑛 ≤ 104
Output:
Return an integer that represents the number of substrings of s that contain exactly k distinct characters.
Examples:
Example 1
Input: s = "pqpqs", k = 2
Output: 7
Explanation: The possible substrings with exactly 2 distinct characters are: "pq", "pqp", "qp", "pqs", "pq", "qs", and "pq". Thus, there are 7 such substrings.
'''
def day14_sol(s, k):
    if k > len(s):
        return 0
    def max_length(k):
        d = {}
        count = 0
        left = 0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            while len(d) > k:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left+= 1
            count += i - left + 1
        return count
        
    return max_length(k) - max_length(k-1)
    
print(day14_sol('pqpqs',2))
