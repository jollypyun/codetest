# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/159994

from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    while goal:
        word = goal.popleft()
        if cards1 and word == cards1[0]:
            cards1.popleft()
        elif cards2 and word == cards2[0]:
            cards2.popleft()
        else:
            return 'No'
        
    return 'Yes'

'''
해당 문제는 두 개의 카드 뭉치에서 각 첫번째 인덱스에 해당하는 단어를 뽑아서 goal의 순서대로 만드는 것이다.

이것을 반대로 생각해서 풀면 된다.
goal의 첫번째 인덱스를 뽑아 각 카드 뭉치의 첫번째 인덱스를 비교하는 방식으로 하면 쉽게 풀린다.
'''
