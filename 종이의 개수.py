# 링크 : https://www.acmicpc.net/problem/1780
# 시간 : 4200ms, 공간 : 69640KB
import sys
ssr = sys.stdin.readline

n = int(ssr())
board = [list(map(int, ssr().rstrip().split(' '))) for _ in range(n)] 
result = [0,0,0]

def solution(x,y,k):
  color = board[x][y]
  for i in range(x, x+k):
    for j in range(y, y+k):
      if color != board[i][j]:
        div = k // 3
        solution(x,y,div)
        solution(x,y+div,div)
        solution(x,y+(2*div),div)
        solution(x+div,y,div)
        solution(x+div,y+div,div)
        solution(x+div,y+(2*div),div)
        solution(x+(2*div),y,div)
        solution(x+(2*div),y+div,div)
        solution(x+(2*div),y+(2*div),div)
        return
  
  if color == -1:
    result[0] += 1
  elif color == 0:
    result[1] += 1
  else:
     result[2] += 1

solution(0,0,n)
print(result[0], result[1], result[2], sep='\n')
