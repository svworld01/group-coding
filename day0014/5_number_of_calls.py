# created by KUMAR SHANU

# 5. Number of Recent Calls
# https://leetcode.com/problems/number-of-recent-calls/


class RecentCounter:
    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.pop(0)
        return len(self.q)
