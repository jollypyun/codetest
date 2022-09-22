# https://www.acmicpc.net/problem/25305
# 68ms, 30840kB

import sys
ssr = sys.stdin.readline

n, k = map(int, ssr().split(' '))
lst = list(map(int, ssr().split(' ')))
lst.sort(reverse=True)
print(lst[k-1])
