
/*solution by  :  Vivek pandey

problem link  : https://leetcode.com/problems/shuffle-the-array/


approach 
    taking a new array;
    inserting element in array like new arr[0] = prev arr[0], new arrr[1] = prev arr[n]......and so..on
    
    
*/

class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector <int> v;
        for(int i=0;i<n;i++){
            v.push_back(nums[i]);
            v.push_back(nums[i+n]);
        }
        return v;
    }
};
