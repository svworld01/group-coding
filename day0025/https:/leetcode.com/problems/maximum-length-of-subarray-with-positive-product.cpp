/* code by : vivek pandey 


problem link : https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

approach :  Two pointer inplementation

*/


Solution :



class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        int pos=0,neg=0;
        int ans=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                
                neg=0;
                pos=0;
            }
            else if(nums[i]<0){
                swap(pos,neg);
                neg +=1;
                if(pos!=0){
                    pos +=1;
                }
                ans = max(ans,pos);
            }
            else{
                pos +=1;
                if(neg !=0){
                    neg +=1;
                }
                ans = max(ans,pos);
            }
        } 
        return ans;
    }
};
