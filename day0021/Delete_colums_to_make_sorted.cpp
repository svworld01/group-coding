/* code by : Vivek pandey

Problem link : https://leetcode.com/problems/delete-columns-to-make-sorted



Solution 

*/

class Solution {
public:
    int minDeletionSize(vector<string>& A) {
        int len = A[0].size();
        int cnt = A[0].size();
        for(int i=0;i<len;i++){
            for(int j=1;j<A.size() && A[j][i]>=A[j-1][i];j++){
                if(j==A.size()-1){
                    cnt--;
                }
            }
        }
        return cnt;
    }
};
