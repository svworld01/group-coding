# created by KUMAR SHANU

# 4. Count Number of Teams
#https://leetcode.com/problems/count-number-of-teams/


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        l = len(rating)
        count = 0
        for i in range(l-2):
            for j in range(i+1, l-1):
                for k in range(j+1, l):
                    if(rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                        #print(rating[i],rating[j],rating[k])
                        count += 1
        return count
        
