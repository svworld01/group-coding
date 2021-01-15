# created by KUMAR SHANU

# 1. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/


class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        l, r = 0, len(arr) - 1
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        if s == ' ' * len(s):
            return s
        while l <= r:
            if arr[l] not in vowels:
                l += 1
                continue
            if arr[r] not in vowels:
                r -= 1
                continue

            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return ''.join(arr)
