# 시간 : 68ms
# 코드 길이 : 329B
# 링크 : https://www.acmicpc.net/problem/2004

import sys
ssr = sys.stdin.readline

def counting(n):
  n1, n2 = n,n
  cnt_2, cnt_5 = 0, 0
  while n1 != 0:
    n1 //= 2
    cnt_2 += n1
  while n2 != 0:
    n2 //= 5
    cnt_5 += n2
  return cnt_2, cnt_5

a,b = list(map(int, ssr().split()))
c = a-b
u,v = counting(a)
w,x = counting(b)
y,z = counting(c)

print(min(u-w-y, v-x-z))
