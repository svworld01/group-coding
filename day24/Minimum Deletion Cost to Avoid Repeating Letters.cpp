  /*
  code by : vivek pandey
  
  solution 
  */
  
  class Solution {
public:
    int minCost(string s, vector<int>& cost) {
        stack<char> c;
        stack<int> d;
        int i=0;
        int n= s.size();
         if(i==0){
                c.push(s[i]);
                d.push(cost[i]);
            }
        int cnt=0;
        i=i+1;
        while(i<n){
            
                if(c.top()==s[i]){
                    int t= d.top();
                    cnt += t<cost[i]?t:cost[i];
                    if(t<cost[i]){
                        d.pop();
                        d.push(cost[i]);
                    }
                }
                else{
                    c.push(s[i]);
                    d.push(cost[i]);
                }
            
            i++;
        }
        return cnt;
    }
};
