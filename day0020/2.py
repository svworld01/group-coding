# created by KUMAR SHANU

# 2. Assign Cookies
# https://leetcode.com/problems/assign-cookies


# Solution 1
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        count = 0
        i, j = 0, 0
        while i < len(g):

            while j < len(s):
                if s[j] >= g[i]:
                    count += 1
                    j += 1
                    break
                j += 1

            if j == len(s):
                break
            i += 1
        return count


# Solution 2
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """Assign coockies to childrens and find the total number

        Args:
            g (List[int]): Array of children
            s (List[int]): Array of coockies

        Returns:
            int: total number of child who get coockies.
        """
        g.sort()
        s.sort()
        i, j = len(g) - 1, len(s) - 1
        while (i >= 0 and j >= 0):
            if g[i] <= s[j]:
                j -= 1
            i -= 1
        return len(s) - j - 1
