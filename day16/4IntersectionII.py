# created by KUMAR SHANU

# 4. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii
"""

Optimal Solution: Intersection of Sorted Arrays

"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Sort both the arrays
        nums1.sort()
        nums2.sort()

        # initialize empty set
        arr = []

        # initialize the two pointers
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1

            elif nums2[j] < nums1[i]:
                j += 1

            else:
                arr.append(nums2[j])
                j += 1
                i += 1

        return list(arr)


"""

Optimal Solution : Using Hash

"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_dict = dict()
        res = []
        for i in nums2:
            if i in my_dict:
                my_dict[i] += 1

            else:
                my_dict[i] = 1

        for i in nums1:
            if i in my_dict and my_dict[i] > 0:
                res.append(i)
                my_dict[i] -= 1

        return res
