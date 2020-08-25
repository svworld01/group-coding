/*
        **Auther Akash **
        **Approch***
        if a number is power of four then this number is never going to return non Zero reminder after devide.so after using % oprator for checking reminder and reduce the number by deviding by four     :)#happy Coding


*/


public class Solution{
public boolean isPowerOfFour(int num) {
    while(num>0){
        if(num==1){
            return true;
        }
 
        if(num%4!=0){
            return false;
        }else{
            num=num/4;
        }
    }
 
    return false;
}
    }
