# created by KUMAR SHANU

# 5. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/


def check(speed: int, piles: List[int]) -> int:
    # check the hours required to eat all piles
    # with given speed
    hours = 0
    for p in piles:
        hours += (p + speed - 1) // speed
    return hours


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # Apply binary search on speed
        # L will be min speed i.e. 1
        # R will be max speed i.e. max(piles)
        L, R = 1, max(piles)
        ans = R
        while L <= R:
            mid = (L + R) // 2

            if (check(mid, piles) <= H):
                ans = min(ans, mid)
                R = mid - 1
            else:
                L = mid + 1
        return ans
