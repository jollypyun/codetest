# 시간 : 116ms
# 코드 길이 : 178B
# 링크 : https://www.acmicpc.net/problem/10773

# deque를 사용한 것보다 일반 list를 사용하는 것이 더 빠르다.

import sys
ssr = sys.stdin.readline

k = int(ssr())
lst = []
for _ in range(k):
  num = int(ssr())
  lst.pop() if(len(lst) != 0 and num == 0) else lst.append(num)
print(sum(lst))
