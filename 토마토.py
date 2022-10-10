# 링크 : https://www.acmicpc.net/problem/7576
# 시간 : 2140ms, 메모리 : 106192KB

import sys
from collections import deque
ssr = sys.stdin.readline

m,n = list(map(int, ssr().split(' ')))
matrix = [list(map(int, input().split(' '))) for _ in range(n)]
q = deque([])
dx, dy = [1,0,-1,0], [0,1,0,-1]
answer = 0

for i in range(n):
  for j in range(m):
    if matrix[i][j] == 1:
      q.append([i,j])

def bfs():
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx, ny = dx[i] + x, dy[i] + y
      if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
        matrix[nx][ny] = matrix[x][y] + 1
        q.append([nx,ny])

bfs()
for i in matrix:
  for j in i:
    if j == 0:
      print(-1)
      exit(0)
  answer = max(answer, max(i))
print(answer - 1)
