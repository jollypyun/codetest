# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/70129?language=python3

def solution(s):
    cnt = 0
    removal = 0
    while True:
        if s == '1':
            return [cnt, removal]
        removal += s.count('0')
        s = bin(len(s.replace('0', '')))[2:]
        cnt += 1

'''
0의 개수를 구하는 count 함수와 이진 변환 함수인 bin을 이용한다.
0을 삭제하는 것은 replace 함수를 이용해서 0을 모두 삭제한다.
'''
