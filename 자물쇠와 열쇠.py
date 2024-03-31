# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/60059

def rotate_key(key):
    n = len(key)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = key[i][j]
    return result

def check(new_lock, lock_len):
    for i in range(lock_len, lock_len*2):
        for j in range(lock_len,lock_len*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    key_len = len(key)
    lock_len = len(lock)
    new_lock = [[0] * (lock_len * 3) for _ in range(lock_len * 3)]
    for i in range(lock_len):
        for j in range(lock_len):
            new_lock[i+lock_len][j+lock_len] = lock[i][j]

    for _ in range(4):
        key = rotate_key(key)
        for i in range(1, lock_len * 2):
            for j in range(1, lock_len * 2):
                for x in range(key_len):
                    for y in range(key_len):
                        new_lock[i+x][j+y] += key[x][y]
                
                if check(new_lock, lock_len):
                    return True
                else:
                    for x in range(key_len):
                        for y in range(key_len):
                            new_lock[i+x][j+y] -= key[x][y]
    return False


'''
1. new_lock은 기존 lock에 비해 3배 크게 한다. 이유는 다음과 같다.
- 열쇠는 최대 크기가 자물쇠 크기이다. 하지만 열쇠의 일부만으로 자물쇠를 전부 1로 덮을 수 있다.
- 그렇기 때문에 열쇠를 왼쪽 위부터 오른쪽 아래까지 탐색을 해야하기 때문이다.
- 열쇠의 사이즈를 고려하여 자물쇠의 3배 큰 lock을 만든다.

2. 열쇠를 회전시킬 수 있기 때문에 회전된 열쇠도 고려해서 4번 순회한다.
3. 새로 만든 lock 중 실제 자물쇠가 해당된 영역이 1로만 되어 있어야 한다. 0은 비어있는 것이고 1이 넘은 값은 안 맞는 부분이기 때문이다.
4. 하나라도 맞으면 true, 아니면 false
'''
