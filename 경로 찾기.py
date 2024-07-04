# 링크: https://www.acmicpc.net/problem/11403
# 메모리: 34052 KB
# 시간: 88 ms

from collections import defaultdict, deque
import sys

ssr = sys.stdin.readline
n = int(ssr())
d = defaultdict(list)

for i in range(n):
  l = list(map(int, ssr().split(' ')))
  for j in range(n):
    if l[j] == 1: d[i].append(j)

for i in range(n):
  flags = [0] * n
  q = deque(d[i])
  while q:
    a = q.popleft()
    if flags[a] == 0: 
      flags[a] = 1
      q.extend(d[a])

  print(' '.join(map(str, flags)))

# 해당 문제는 일단 경로를 정리한 후 bfs 로 풀었다.
