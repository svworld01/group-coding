/*
Auther -  Anand
*/

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
       int a[101]={0,0};
       for(int i=0;i<nums.size();i++)
       {
           a[nums[i]]++;
       }
        int sum=0;
        for(int i=1;i<101;i++)
        {
            sum+=((a[i]*(a[i]-1))/2);
        }
        return sum;
    }
};
