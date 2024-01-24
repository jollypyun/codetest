# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/135807

def gcd_(a,b):
    while b > 0:
        a,b = b,a%b
    return a

def gcd_arr(arr):
    gcd = arr[0]
    for item in arr:
        gcd = gcd_(gcd, item)        
    return gcd

def solution(arrayA, arrayB):
    answer = 0
    gcd_a, gcd_b = 0, 0
    
    gcd_a = gcd_arr(arrayA)
    gcd_b = gcd_arr(arrayB)
    for a in arrayA:
        if a%gcd_b == 0:
            gcd_b = 0
            break
    for b in arrayB:
        if b%gcd_a == 0:
            gcd_a = 0
            break
            
    return max(gcd_a, gcd_b)


'''
유클리드 호제법을 이용해서 최대 공약수를 구한다.
'''
