# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/178871#

# 실패 사례 1 (9~13 시간 초과 실패) : 단순 스왑
def solution(players, callings):
    for i in callings:
        idx = players.index(i)
        temp = players[idx]
        players[idx] = players[idx-1]
        players[idx-1] = temp
    return players

# 실패 사례 2 (7~13 시간 초과 실패): dict, list 활용
def solution(players, callings):
    d = {j:i for i,j in enumerate(players)}
    for i in callings:
        past = [k for k,v in d.items() if v == d[i] - 1].pop()
        d[past] += 1
        d[i] -=1
    
    return list(map(lambda y: y[0], sorted(d.items(), key = lambda x: x[1])))
