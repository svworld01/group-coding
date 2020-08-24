# created by KUMAR SHANU

# 1. Sort Integers by The Number of 1 Bits
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return self.bubbleSort(arr, len(arr))

    def bubbleSort(self, arr, l):
        for i in range(l - 1):
            bc1 = self.countBits(arr[i])
            bc2 = self.countBits(arr[i + 1])
            if (bc1 > bc2) or (bc1 == bc2 and arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        if l == 0:
            return arr
        return self.bubbleSort(arr, l - 1)

    def countBits(self, num):
        num = str(bin(num))

        return num.count('1')
