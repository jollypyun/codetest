# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/92335

import math

def make_convert(n,k):
    num = ''
    while n > 0:
        n, r = divmod(n, k)
        num += str(r)
    return num[::-1]

def check_prime(n):
    n = int(n)
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    convert = make_convert(n,k)
    if convert.count('0') == 0:
        is_prime = check_prime(convert)
        return 1 if is_prime else 0
    
    l = convert.split('0')    
    while '' in l:
        l.remove('')
    
    answer = 0
    for i in l:
        answer += 1 if check_prime(i) else 0
    return answer

'''
소수 판별 알고리즘, 진수 변환 방법을 알고 있어야 효율성에서도 통과할 수 있다.

소수 판별 알고리즘은 약수의 성질을 알고 있어야 한다.
어떤 수 n 에 대해서 소수를 구하고자 할 때, 
n의 제곱근을 기준으로 해서 대칭성을 가지고 있기 때문에 2부터 n 까지 순회를 돌 필요성이 없다.
2부터 n 의 제곱근까지만 순회를 하면 된다.
이로 인해 얻을 수 있는 시간 복잡도는 O(N^1/2) 이다.
'''