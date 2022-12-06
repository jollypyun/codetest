# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/77486

from collections import defaultdict

def uf(parent, earn, now, cost):
    up = cost // 10
    if up < 1 or parent[now] == now:
        earn[now] += cost
        return
    mine = cost - up
    earn[now] += mine
    uf(parent, earn, parent[now], up)
    

def solution(enroll, referral, seller, amount):
    l = len(enroll)
    answer = [0] * (l+1)
    d = defaultdict()
    parent = [i for i in range(l+1)]
    for i in range(l):
        d[enroll[i]] = i + 1
    for i in range(l):
        p = referral[i]
        if p == '-':
            parent[i+1] = 0
        else:
            parent[i+1] = d[p]
    
    for i, j in zip(seller, amount):
        uf(parent, answer, d[i], j * 100)
    return answer[1:]
