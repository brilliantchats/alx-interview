#!/usr/bin/python3
"""
Returns the Pascal's Triangle
"""


def pascal_triangle(n):
    """ Retruns pascal's triangle """
    finalArr = list()
    if n <= 0:
        return finalArr
    finalArr.append([1])
    for i in range(n - 1):
        arr = list()
        prevArr = finalArr[i]
        for j in range(len(prevArr) + 1):
            if j == 0:
                arr.append(prevArr[j])
            elif len(prevArr) == 1:
                arr.append(prevArr[0])
            elif j == len(prevArr):
                arr.append(prevArr[len(prevArr) - 1])
            else:
                arr.append(prevArr[j - 1] + prevArr[j])
        finalArr.append(arr)
    return finalArr
