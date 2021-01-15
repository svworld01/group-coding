# created by KUMAR SHANU

# 5. Task Scheduler
# https://leetcode.com/problems/task-scheduler

from collections import defaultdict


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # intialize dictionary(Hash)
        d = defaultdict(int)

        # count frequency of each task
        for task in tasks:
            d[task] += 1

        # sort the frequencies from max to min
        d = sorted(d.values(), key=lambda x: -x)

        # calculate max value
        max_val = d[0] - 1

        # calculate the no of free spaces
        idle_slots = max_val * n

        # filling the spaces by tasks
        for i in range(1, len(d)):
            idle_slots -= min(d[i], max_val)

        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)
