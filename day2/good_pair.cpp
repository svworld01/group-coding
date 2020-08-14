
    /* solved by : vivek pandey
    problem link :  https://leetcode.com/problems/number-of-good-pairs.
    
    class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        
//good pair

	sort(nums.begin(),nums.end());
	 
	int sum =0;
    int cnt =1;
	for(int i=0;i<nums.size()-1;i++){
        if(nums[i]==nums[i+1]){
            cnt++;
        }    
        else{
            sum += cnt*(cnt-1)*0.5;
            cnt=1;
        }
    }
        if(cnt>1){
            sum +=cnt*(cnt-1)*0.5;
        }
        
	return sum;
    }
};
