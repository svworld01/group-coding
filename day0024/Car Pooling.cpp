/* code by :Vivek pandey

problem link : https://leetcode.com/car_pooling/

solution */

class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        int a[1001] = {0};
        for(int i=0;i<trips.size();i++){
            int aa= trips[i][0];
            int b= trips[i][1];
            int c= trips[i][2];
            for(int j=b;j<c;j++){
                a[j] += aa;
            } 
        }
        
          bool ans = true;
            for(int i=0;i<1001;i++){
                if(a[i]>capacity){
                    return false;
                }
            }
        return true;
    }
};
