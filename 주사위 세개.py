# 링크 : https://www.acmicpc.net/problem/2480
# 시간 : 88ms
# 메모리 : 32424KB
# 코드 길이 : 386B

from collections import Counter
import sys
ssr = sys.stdin.readline

answer = 0
lst = list(map(int, ssr().split(' ')))
dict = Counter(lst)

keys = list(dict.keys())
values = list(dict.values())

if max(values) == 1:
  answer = max(keys) * 100
elif max(values) == 2:
  a = values.index(max(values))
  answer = 1000 + 100 * keys[a]
else:
  answer = 10000 + 1000 * keys[0]
  
print(answer)
