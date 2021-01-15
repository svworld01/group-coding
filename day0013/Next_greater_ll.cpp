
/*
code by : Vivek pandey
*/

class Solution {
public:
    
    
    vector<int> nextGreaterElements(vector<int>& nums) {
        //int max =0;
        int n = nums.size();
         
        vector<int > v(n,-1);
        for(int i=0;i<n;i++){
                 for(int j=i+1;j%n!=i;j++){
                     if(nums[j%n]>nums[i]){
                         v[i] = nums[j%n];
                         break;
                     }
                 }
        }
        return v;
    }
};
