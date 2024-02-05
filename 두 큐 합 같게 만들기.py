# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    limit = len(queue1) * 4
    tot1 = sum(q1)
    tot2 = sum(q2)
    
    while True:
        if answer > limit:
            return -1
        
        if tot1 > tot2:
            a = q1.popleft()
            q2.append(a)
            tot1 -= a
            tot2 += a
        elif tot2 > tot1:
            a = q2.popleft()
            q1.append(a)
            tot2 -= a
            tot1 += a
        else: return answer
        answer += 1

'''
1. limit를 큐의 길이의 4배로 정해놓은 이유는 숫자를 옮기는 행위를 통해서 queue1, queue2 각각 모습이 다시 만들어지기 위해서는 queue1의 길이의 4배에 해당하는 횟수를 통해 이뤄지기 때문이다.
2. queue1, queue2 길이가 같아야하므로 비교 후 이동 혹은 return을 하면 된다.
'''
