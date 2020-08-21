
/* 

code by : Vivek pandey

*/

class Solution {
public:
    int integerReplacement(long long int n) {
      if(n==0)
          return 1;
        if(n==1)
            return 0;
        
    
    long long int cnt =0; 
    while(n!=1){
	    int t = n & 1;
	    if(t==1){
            if(n==3){   //according to condition 
                n= 2;
            }
		else if((n+1)%4==0){
            n = n+1;
        }
            else{
                n = n-1;
            }
		cnt++;
	        }
        
	    else{
		n = n>>1;
		cnt++;
	        }
	
    }
return cnt;
    }
};
