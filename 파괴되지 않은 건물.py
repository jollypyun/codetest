# 누적합 알고리즘을 사용해야 하는 문제
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    n, m = len(board), len(board[0])
    temp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for typ, r1, c1, r2, c2, degree in skill:
        temp[r1][c1] += degree if typ == 2 else -degree
        temp[r1][c2+1] += -degree if typ == 2 else degree
        temp[r2+1][c1] += -degree if typ == 2 else degree
        temp[r2+1][c2+1] += degree if typ == 2 else -degree
    
    for i in range(n):
        for j in range(1, m):
            temp[i][j] += temp[i][j-1]
            
    for j in range(m):
        for i in range(1,n):
            temp[i][j] += temp[i-1][j]
    
    return sum(board[i][j] + temp[i][j] > 0 for i in range(n) for j in range(m))
