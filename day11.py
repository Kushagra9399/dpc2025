'''
You are given a string s. Your task is to generate and return all possible permutations of the characters in the string. A permutation is a rearrangement of the characters in the string, and each character must appear exactly once in every permutation. If there are duplicate characters in the string, the resulting permutations should also be unique (i.e., no repeated permutations).

Input:
A string s consisting of lowercase English letters. The length of the string n satisfies 1≤𝑛≤9.

Output:
An array of strings containing all unique permutations of the input string. The order of permutations in the output does not matter.

Examples:
Example 1
Input: "abc"
Output: ["abc", "acb", "bac", "bca", "cab", "cba"]
Explanation: All possible arrangements of "abc" are listed, and there are no duplicate permutations.
'''
def day11_sol(s):
    d = {}
    result = set()
  
    def recurse(curr):
        if len(curr) == len(s):
            result.add(curr)
        return
        for i in d:
            if d[i] > 0:
                d[i] -= 1 
                recurse(curr + i)
                d[i] += 1
        return
  
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    recurse("")
    return list(result)
  
print(day11_sol("abc"))
