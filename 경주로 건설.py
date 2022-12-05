# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(board, direction):
    l = len(board)
    price = [[int(1e9)] * l for _ in range(l)]
    price[0][0] = 0
    q = deque()
    q.append((0,0,0,direction))
    
    while q:
        x,y,cost,d = q.popleft()
        if x == l-1 and y == l-1:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (nx < 0 or ny < 0 or nx > l-1 or ny > l-1) or ((d+2) % 4 == i) or (board[ny][nx] == 1):
                continue
            temp = cost + 100 if i == d else cost + 600
            
            if price[ny][nx] > temp:
                price[ny][nx] = temp
                q.append((nx, ny, temp, i))

    return price[l-1][l-1]
def solution(board):
    return min(bfs(board,0), bfs(board,1))
