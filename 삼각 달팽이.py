# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    num = 1
    board = [[0] * n for _ in range(n)]
    x = -1
    y = 0
    answer = []
    
    for i in range(n):
        for j in range(i,n):
            if i%3==0:
                x += 1
            elif i%3==1:
                y += 1
            elif i%3==2:
                x -= 1
                y -= 1
            
            board[x][y] = num
            num += 1
    for i in range(n):
        for j in range(i+1):
            answer.append(board[i][j])
    return answer

'''
답을 봤기 때문에 다시 보자. (2024/02/09)
원리를 파악하는 것부터 실패했다.
'''
