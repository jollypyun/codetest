# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# 48 ms 14.7 MB

class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(' ')
        lst = [i[::-1] for i in lst]
        return ' '.join(lst)
