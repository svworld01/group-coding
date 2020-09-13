/* code by : Vivek pandey

approach : Greedy
*/


class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int n = bills.size();
        int a=0,b=0;
        for(int i=0;i<n;i++){
            int t= bills[i];
            if(t==5){
                a++;
            }
            else if(t==10){
                if(a<=0)
                    return false;
                else
                    b++;
                    a = a -1;
            }
            else{
                if(a>=1 && b>=1){
                    b=  b-1;
                    a = a-1;
                }
                else if(a>=3){
                    a= a-3;
                }
                else
                    return false;
            }
        }
        return true;
    }
};
