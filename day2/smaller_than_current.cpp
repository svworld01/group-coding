/*
  solved by : vivek pandey
  
  problem link : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number.
  
  */
  class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        
	//smaller number

	vector<int> v;
	int n=  nums.size();
	for(int i=0;i<n;i++){
		int cnt=0;
		for(int j=0;j<n;j++){
			if(i!=j){
				if(nums[i]>nums[j]){
					cnt++;
				}
			}
		}
		v.push_back(cnt);
	}
	return v;
    }
};
