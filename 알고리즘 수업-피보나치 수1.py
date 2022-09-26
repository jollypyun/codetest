# https://www.acmicpc.net/problem/24416
# 68ms, 30840KB

import sys
ssr = sys.stdin.readline

n = int(ssr())
lst = [1 for _ in range(n+1)]
for i in range(3, n+1):
  lst[i] = lst[i-1] + lst[i-2]

print(lst[n], n-2)
