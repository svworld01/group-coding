/*
code by : vivek pandey

*/




class Solution {
public:
    bool isPowerOfFour(long long int num) {
     

/// bool ispowerofpower
	    bool ans ;
        if(num==0){
            ans = false;
        }
      else  if((num & (num-1))==0){
	        int cnt =0;
	    while(num){
		    if((num & 1)==0){
			cnt++;
		    }
		    num >>= 1;
	    }
	        if(cnt%2==0){
		    ans = true;
	        }
            
	        else{
		    ans = false;
	        }
 
        }
        
        else{
	    ans = false;
            }
        return ans;   
    }
};
