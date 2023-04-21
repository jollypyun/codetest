# 링크 : https://www.acmicpc.net/problem/11659
# 시간 : 272ms, 메모리 : 41316KB
# 전형적인 DP 문제

import sys
ssr = sys.stdin.readline

n,m = map(int, ssr().split(' '))
nums = list(map(int, ssr().split(' ')))
lst = [nums[0]] * len(nums)
for i in range(1, len(nums)):
  lst[i] = lst[i-1] + nums[i]

for _ in range(m):
  i,j = map(int, ssr().split(' '))
  print(lst[j-1] - lst[i-2] if i-2 >= 0 else lst[j-1])
