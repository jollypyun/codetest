# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/150369

def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0
    pickup = 0
    
    for i in range(n-1, -1, -1):
        if deliveries[i] != 0 or pickups[i] != 0:
            cnt = 0
            while delivery < deliveries[i] or pickup < pickups[i]:
                delivery += cap
                pickup += cap
                cnt += 1

            delivery -= deliveries[i]
            pickup -= pickups[i]
            
            answer += (i+1)*cnt*2              
    return answer

'''
이것은 다른 사람의 풀이를 봤다.
아무리 봐도 모르기 때문이었다.
근데 이 풀이도 어떻게 나온 풀이인지 모르겠다.
'''
