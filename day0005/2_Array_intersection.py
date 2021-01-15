# created by KUMAR SHANU

# 2. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

## Solution 1
"""
Simple solution using python inbuilt set datastructure
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # convert each array into python's set
        # use intersection operator (&)
        return list(set(nums1) & set(nums2))


## Solution 2
"""
Simple Solution. [Brute Force]
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # initialize empty array
        res = []

        for n1 in nums1:
            for n2 in nums2:

                # check common elements in both arrays
                # if it already present in the resultant array
                # skip it
                if n1 == n2 and n1 not in res:
                    res.append(n1)
                    break
        return res


## Solution 3
"""
Optimal Solution: Using Binary Search.
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # initialize empty set
        res = set()

        # get smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # sort smaller array
        nums1.sort()
        for num in nums2:

            # binary search into sorted array to get common element
            if self.binary_search(nums1, num) != -1:
                res.add(num)

        return list(res)

    def binary_search(self, nums: List[int], target: int) -> int:
        # find boundaries
        l, r = 0, len(nums) - 1

        while l <= r:

            # find middle element
            mid = l + (r - l) // 2

            # base case
            # return index if middle element is equal to target
            if nums[mid] == target:
                return mid

            # if middle element is smaller than target
            # reduce the search to left subarray
            if nums[mid] < target:
                l = mid + 1

            # if middle element is smaller than target
            # reduce the search to left subarray
            else:
                r = mid - 1

        return -1


## Solution 4
"""
Optimal Solution : Using Hash
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # intialize a hash
        # and add all elements of first array into hash
        hs = set(nums1)
        arr = set()
        for num in nums2:

            # search into hash for common elements
            # O(1) search
            if num in hs:
                arr.add(num)
        return list(arr)


## Solution 5
"""
Optimal Solution: Intersection of Sorted Arrays
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Sort both the arrays
        nums1.sort()
        nums2.sort()

        # initialize empty set
        arr = set()

        # initialize the two pointers
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                i += 1

            elif nums2[j] < nums1[i]:
                j += 1

            else:
                arr.add(nums2[j])
                j += 1
                i += 1

        return list(arr)
