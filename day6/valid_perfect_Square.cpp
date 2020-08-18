/*
  Auther- Anand Keshari
  Problem link- https://leetcode.com/problems/valid-perfect-square/
  
  Time Complexity - O(log n)
  space Complexity -  O(log n)
  
  Explanation- Binary search from 1 to n/2;
  and look for mid*mid==num;
  if not then recursively look in left or right part.
*/

bool binary_search(int num, unsigned long long int l, unsigned long long int r)
{
    unsigned long long int mid=l +(r-l)/2;
    if(mid*mid==num)
        return true;
    if(l<r)
    {
        if(mid*mid>num)
        {
            return binary_search(num,l,mid-1);
        }
        if(mid*mid<num)
        {
            return binary_search(num,mid+1,r);
        }
    }
    return false;
}
class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num==1)
            return true;
        unsigned long long int l=1;
        unsigned long long int r = num/2; 
       return binary_search(num, l,r);    
    }
};
