'''
Problem : Longest Common Prefix
You are given an array of strings strs[], consisting of lowercase letters.
Your task is to find the longest common prefix shared among all the strings.
If there is no common prefix, return an empty string "".

Input :
An array of strings strs[] where each string consists of lowercase English letters.
Example: strs[] = ["flower", "flow", "flight"]

Output :
* A string representing the longest common prefix. If no common prefix exists, return an empty string "".
Example: "fl"
'''

def day9(arr):
    if len(arr)==0:
        return ""
    elif len(arr)==1:
        return arr[0]
    else:
        a = arr[0]
        for i in arr:
            b = ""
            for j in range(min(len(a),len(i))):
                if a[j]==i[j]:
                    b+=i[j]
                else:
                    break
            if b == "":
                return ""
            a = b
        return a

print(day9(["flower", "flow", "flight"]))
                
