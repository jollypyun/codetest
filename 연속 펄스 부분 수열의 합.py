# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/161988

def solution(sequence):
    temp = [0]
    for index, value in enumerate(sequence):
        temp.append(temp[-1] + value * [1,-1][index%2])
    return max(temp) - min(temp)


# 해당 문제는 DP 방식으로 푸는 것이 좋다.
