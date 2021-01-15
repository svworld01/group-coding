/*
Solution By - Saurabh Verma
*/
class Solution {
    public int getMaxLen(int[] nums) {
        int pos =0;
        int neg=0;
        int max=0; 
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                pos=0;
                neg=0;
            }
            if(nums[i]>0){
                pos=pos+1;
                neg=neg==0?0:neg+1;
            }else if(nums[i]<0){
                int temp = neg;
                neg=pos+1;
                pos=temp==0?0:temp+1;
                
            }
            max=Math.max(pos,max);
        }
        return max;
    }
}
