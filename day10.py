'''
Problem : Group Anagrams
You are given an array of strings strs[].
Your task is to group all the strings that are anagrams of each other.
An anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.

Input :
strs[] = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output :
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
'''
def anagram(s, d):
    if not len(s):
        for i in d:
            if d[i]!=0:
                return False
        return True
    for i in s:
        if i not in d:
            return False
        if d[i] == 0:
            return False
        d[i] -= 1
    return anagram("", d)
    
def day10(arr):
    l = []
    for i in arr:
        if len(l) == 0:
            l.append([i])
            continue
        d = {}
        for k in i:
            if k in d:
                d[k] += 1
            else:
                d[k] = 1
        found = False
        for j in range(len(l)):
            s = l[j][0]
            if anagram(s, d):
                l[j].append(i)
                found = True
                break
        if not found:
            l.append([i])
    return l

print(day10(["eat", "tea", "tan", "ate", "nat", "bat"]))
