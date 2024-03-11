# 링크:https://school.programmers.co.kr/learn/courses/30/lessons/86971

'''
실패 코드
테스트는 통과했으나 결과는 통과하지 못하였다.

union-find 알고리즘을 이용함.
'''
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, x, y):
#     x = find_parent(parent, x)
#     y = find_parent(parent, y)
#     if x < y:
#         parent[y] = x
#     else :
#         parent[x] = y

# def solution(n, wires):
#     answer = n+1
#     wires = [sorted(wire) for wire in wires]
#     wires.sort()
#     for l in range(len(wires)):
#         parent = [i for i in range(n)]
#         for wire in wires:
#             if wires.index(wire) == l: continue
#             a, b = wire
#             a -= 1
#             b -= 1
#             if find_parent(parent, a) != find_parent(parent, b):
#                 union_parent(parent, a, b)
#         answer = min(answer, abs(parent.count(min(parent)) - parent.count(max(parent))))
#     return answer

# 성공코드
def solution(n, wires):
    answer = n
    subs = [wires[i+1:] + wires[:i] for i in range(len(wires))]

    
    for sub in subs:
        s = set(sub[0])
        for _ in sub:
            for element in sub:
                if set(element) & s:
                    s.update(element)
        answer = min(abs(2 * len(s) - n), answer)
    return answer


'''
완전 탐색 문제이다.

subs 라는 곳에 전선 하나씩 빠진 상태의 리스트들을 담는다.
순회를 돌면서 각 케이스마다 두 그룹마다 송전탑 개수의 차이를 본다.

이중 FOR문 돌면서 한 그룹의 송전탑이 몇개인지 확인한다.
이렇게 돌면서 두 그룹 사이의 차가 최소인 것을 찾는다.
'''
