/*
solved by : vivek pandey

problem link : https://leetcode.com/problems/xor-operation-in-an-array.

*/

    class Solution {
public:
    int xorOperation(int n, int start) {
        

	//xor operation
	//vector<int> v;
	int i=0;
	int p =  start + 2*i;
	int j=0;
	int sum = 0;
	while(j<n){
		sum = sum ^ p;
		i++;
		p = start + 2*i;
		j++;
	}
	return sum;
    }
};
