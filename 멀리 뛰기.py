# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    numbers = [0,1,2,3]
    if(n == 1): return 1
    elif (n == 2): return 2
    elif (n == 3): return 3
    else: 
        for i in range(4, n+1):
            numbers.append(numbers[i-1] + numbers[i-2])
    return numbers[n] % 1234567

# 이런 문제는 규칙을 찾아서 점화식을 찾는 것이 관건이다.
