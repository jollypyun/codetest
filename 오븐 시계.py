# 링크 : https://www.acmicpc.net/problem/2525
# 시간 : 84ms
# 메모리 : 30840KB
# 코드 길이 : 198B

import sys
ssr = sys.stdin.readline

a, b = map(int, ssr().split(' '))
c = int(ssr())
m = b + c
cnt = 0

if m >= 60:
  cnt = m // 60
  m %= 60

h = a + cnt

if h >= 24:
  h -= 24
print(h,m, sep=' ')
