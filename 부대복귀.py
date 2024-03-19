# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132266#

from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    d = defaultdict(list)
    for a,b in roads:
        d[a].append(b)
        d[b].append(a)
    visited = [-1] * (n+1)
    visited[destination] = 0
    
    q = deque([destination])
    
    while q:
        now = q.popleft()
        for i in d[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                q.append(i)
        
    return [visited[i] for i in sources]

'''
1. 먼저는 그래프를 그려준다.
2. 각 노드를 일단 -1로 설정한다.
3. 목적지는 0으로 설정.
4. 목적지서부터 그래프 탐색을 시작한다.
'''
