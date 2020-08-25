# created by KUMAR SHANU

# 2. Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters)
        while low < high:
            mid = low + (high - low) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return letters[low % len(letters)]
