# 링크 : https://www.acmicpc.net/problem/11286
# 시간 : 148ms, 공간 : 39492KB

import sys
import heapq as h
ssr = sys.stdin.readline

n = int(ssr())
lst = []

for _ in range(n):
  num = int(ssr())
  abs_num = abs(num)
  if num !=0:
    h.heappush(lst, (abs_num, num))
  else:
    print(h.heappop(lst)[1]) if len(lst) != 0 else print(0)
