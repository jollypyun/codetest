# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12907#

def solution(n, money):
    money = [i for i in money if n >= i]
    dp = [0] * (n+1)
    dp[0] = 1
    
    for coin in money:
        for idx in range(coin, n+1):
            dp[idx] += dp[idx - coin]
    return dp[n] % 1000000007

'''
dp 문제

동전별로 금액에서 해당 동전의 값만큼 뺀 금액의 가짓수를 해당 금액의 가짓수를 더하는 방법으로 쌓아간다.
예를 들어 5원 거스름돈이고 3원 동전의 경우에는 2원이 필요하므로 2원 거스름돈 가짓수를 더해주는 것으로 한다.
즉, 5원 = (3원 거스름돈 가짓수) + (2원 거스름돈 가짓수)
0번째 인덱스가 1인 이유는 해당 금액의 동전이 있는 경우에는 한 가지 방법밖에 없기 때문이다.
'''
