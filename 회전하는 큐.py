# https://www.acmicpc.net/problem/1021

from collections import deque
import sys

ssr = sys.stdin.readline
n, m = map(int, ssr().split(' '))

q = deque([i for i in range(1, n+1)])
l = list(map(int, ssr().split(' ')))
answer = 0

for num in l:
    while True:
        if q[0] == num:
            q.popleft()
            break
        mid = len(q) // 2
        if mid >= q.index(num):
            q.rotate(-1)
        else:
            q.rotate(1)
        answer += 1

print(answer)

# 큐를 이용하는 문제
