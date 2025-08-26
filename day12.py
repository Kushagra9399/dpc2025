'''
Problem : Valid Parentheses with Multiple Types
You are given a string s consisting of different types of parentheses:(), {}, and [].
Your task is to determine whether the given string is valid.

Input : s = "[{()}]"

Output : true
'''
def day12(s):
    a = []
    for i in s:
        if i=="[" or i=="{" or i=="(":
            a.append(i)
        else:
            if a[-1]=="[" and i=="]":
                a.pop()
            elif a[-1]=="{" and i=="}":
                a.pop()
            elif a[-1]=="(" and i==")":
                a.pop()
            else:
                return False
    if len(a)==0:
        return True
    return False
        
print(day12("[{()}]"))
