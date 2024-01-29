# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    x,y = [(i.index(j), park.index(i)) for i in park for j in i if j == 'S'].pop()
    lx, ly = len(park[0]), len(park)
    d = {'N': [-1,0], 'E': [0,1], 'S': [1,0], 'W': [0,-1]}
    
    for route in routes:
        nx, ny = 0, 0
        direction, move = route.split(' ')
        dy, dx = d[direction]
        for step in range(1, int(move)+1):
            nx = x + dx*step
            ny = y + dy*step
            if nx >= lx or ny >= ly or nx < 0 or ny < 0 or park[ny][nx] == 'X':
                nx, ny = x, y
                break
        x = nx
        y = ny
    return [y,x]

'''
보드 문제이나 그냥 보이는대로 하면 쉽게 할 수 있다.
범위도 적어서 브루탈로 해도 괜찮다.
'''
