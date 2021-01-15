# created by KUMAR SHANU


# 3. Lemonade Change
# https://leetcode.com/problems/lemonade-change
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            # count change of 5$
            if bill == 5:
                five += 1
            # count 10$ and return 5$ back
            elif bill == 10:
                # if don't have 5$ to return
                if five == 0:
                    return False
                five -= 1
                ten += 1
            # Give change back of 10$ and 5$ and other
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
