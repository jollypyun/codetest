# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    return [[sum(a*b for a,b in zip(col, row)) for col in zip(*arr2)] for row in arr1]
