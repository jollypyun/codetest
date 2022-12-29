# 링크 : https://www.acmicpc.net/problem/1992
# 시간 : 48ms, 공간 : 30616KB

import sys
ssr = sys.stdin.readline

n = int(ssr())
board = [list(map(int, ssr().rstrip())) for _ in range(n)]
string = []

def solution(x,y,k):
  color = board[x][y]
  
  for i in range(x, x+k):
    for j in range(y, y+k):
      if color != board[i][j]:
        string.append('(')
        div = k // 2
        solution(x, y, div)
        solution(x, y+div, div)
        solution(x+div, y, div)
        solution(x+div, y+div, div)   
        string.append(')')
        return

  if color == 1:
    string.append('1')
  else:
    string.append('0')

solution(0,0,n)
print(''.join(string))
