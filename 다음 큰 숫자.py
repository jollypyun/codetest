# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    cnt = str(bin(n)).count('1')
    
    for i in range(n+1, 1000001):
        if str(bin(i)).count('1') == cnt:
            return i

'''
bin 함수를 활용할 줄 알아야 한다.
범위가 크다고 해서 겁먹지 말 것. 저장하는 방식이 아니라 순회만 시키면 된다.
'''