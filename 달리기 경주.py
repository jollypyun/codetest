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

# 성공 사례 - 순위에 대한 dict, player에 대한 dict 두 개를 활용해서 pop과 같은 시간이 오래 걸리는 탐색이나 변환 등 작업 시간을 줄인다. 또한, list가 아닌 dict를 사용해 탐색의 시간 복잡도를 줄인다.
def solution(players, callings):
    value_dict = {value: index for index, value in enumerate(players)}
    index_dict = {index: value for index, value in enumerate(players)}
    
    for player in callings:
        idx = value_dict[player]
        past_player = index_dict[idx-1]
        value_dict[player] -= 1
        value_dict[past_player] += 1
        index_dict[idx] = past_player
        index_dict[idx-1] = player
    return list(index_dict.values())
