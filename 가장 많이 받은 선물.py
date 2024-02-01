# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/258712

from itertools import combinations

def solution(friends, gifts):
    histories = dict()
    score = dict()
    nextMonth = dict()
    
    for friend1 in friends:
        histories[friend1] = dict()
        nextMonth[friend1] = 0
        score[friend1] = 0
        for friend2 in friends:
            if friend1 != friend2:
                histories[friend1][friend2] = 0
                
    for gift in gifts:
        giver, receiver = gift.split(' ')
        histories[giver][receiver] += 1
        score[giver] += 1
        score[receiver] -= 1
        
    comb = list(combinations(friends, 2))
    for p1, p2 in comb:
        if histories[p1][p2] == histories[p2][p1]:
            if score[p1] > score[p2]: nextMonth[p1] += 1
            elif score[p1] < score[p2]: nextMonth[p2] += 1
        else:
            if histories[p1][p2] > histories[p2][p1]:
                nextMonth[p1] += 1
            else:
                nextMonth[p2] += 1
    return max(list(nextMonth.values()))


'''
해당 문제는 보기에는 복잡해 보인다.
그러나, 변수 선언을 적절히 하면 쉽게 풀 수 있는 문제이다.
이중 dict를 만들어서 하면 시간 초과가 나지 않을까 하지만 최대 범위가 50이고 이에 따라 최대 경우의 수도 1225이기 때문에 시간 초과는 신경쓰지 않고 반복문을 써도 된다.
'''