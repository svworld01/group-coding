# created by KUMAR SHANU

# 3. Repeated DNA Sequences
# https://leetcode.com/problems/repeated-dna-sequences/

from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # dictionary to store frequencies
        d = defaultdict(int)
        for i in range(len(s) - 9):
            # find substring of length 10
            d[s[i:i + 10]] += 1
        #print(d)
        return [i for i in d if d[i] > 1]
