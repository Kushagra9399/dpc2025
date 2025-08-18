'''
Problem : Merge Two Sorted Arrays
You are given two sorted arrays arr1 of size m and arr2 of size n. Your task is to merge these two arrays into a single sorted array without using any extra space (i.e., in-place merging). The elements in arr1 should be merged first, followed by the elements of arr2, resulting in both arrays being sorted after the merge.

Input :
Two sorted integer arrays arr1 of size m and arr2 of size n.
Example : 
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

Output :
Both arr1 and arr2 should be sorted after the merge. Since you cannot use extra space, the final result will be reflected in arr1 and arr2.
Example:
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
'''
import math

def day4_sol(arr1, arr2):
    n, m = len(arr1), len(arr2)
    total = n + m
    gap = (total + 1) // 2
    while gap > 0:
        i, j = 0, gap
        while j < total:
            if i < n:
                a_i = arr1[i]
            else:
                a_i = arr2[i - n]
            if j < n:
                a_j = arr1[j]
            else:
                a_j = arr2[j - n]
            if a_i > a_j:
                if i < n and j < n:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                elif i < n and j >= n:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]
                else:
                    arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]
            i += 1
            j += 1
        if gap == 1:
            break
        gap = (gap + 1) // 2

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
day4_sol(arr1, arr2)
print("arr1:", arr1)
print("arr2:", arr2)
