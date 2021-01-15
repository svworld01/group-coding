# created by KUMAR SHANU

# 4. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/

from bisect import bisect
from collections import defaultdict


class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # dictionary to store values
        self.values = defaultdict(list)
        # dictionary to store timestamps
        self.times = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the value to the dictionary
        self.values[key] += [value]
        # Append the timestamps to the dictionary
        self.times[key] += [timestamp]

    def get(self, key: str, timestamp: int) -> str:

        # Apply binary search on timestamps to get index
        i = bisect(self.times[key], timestamp)
        if i == 0:
            return ""
        else:
            return self.values[key][i - 1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
