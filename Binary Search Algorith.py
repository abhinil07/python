import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def binarySearch(arr, start, end, a):
    if end >= start:
        mid = (end + start)//2
        if arr[mid] == a:
            return mid
        elif arr[mid] > a:
            return binarySearch(arr, start, mid-1, a)
        else:
            return binarySearch(arr, mid+1, end, a)
    else:
            return -1
n = int(input("Enter no of integers in array:"))
arr = []
for i in range(n):
    a = int(input("Enter the integers :"))
    arr.append(a)
arr.sort()
print(arr)
key = int(input("Enter the integer you want to search in th list:"))
lower = 0
higher = n
k = binarySearch (arr, lower, higher, key)
print(k)
