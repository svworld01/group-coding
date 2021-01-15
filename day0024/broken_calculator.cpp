/* code by :Vivek pandey

problem link :  https://leetcode.com/problems/broken-calculator/

solution */

class Solution {
public:
    int brokenCalc(int x, int y) {
        int cnt=0;
        if(x>y){
            return x-y;
        }
        else{
          while(1){
              if(x>=y){
                  cnt += x-y;
                  return cnt;
              }
              else if(y%2){
                  cnt++;
                  y =y+1;
              }
              else{
                  cnt++;
                  y=y/2;
              }
          }  
        }
        return cnt;
    }
};
