/*swapping will help you in 
simplifying the pointer handling  */ 

void swap(int &a, int &b)
{
    int temp=a;
    a=b;
    b=temp;
}
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int ptr1=0,ptr2=0;
        while(ptr2<nums.size())
        {
            if(nums[ptr1]!=val)
            {
                ptr1++;
            }
            else
            {
                if(nums[ptr2]!=val)
                {
                    swap(nums[ptr1],nums[ptr2]);
                    ptr1++;
                }
            }
            ptr2++;
        }
        return (ptr1);
    }
};
