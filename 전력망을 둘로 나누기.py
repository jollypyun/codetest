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
