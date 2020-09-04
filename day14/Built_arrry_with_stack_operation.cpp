/*
code by:  vivek pandey

*/


class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
            //bulid array

	vector<string> ans;
	int index =1;
	if(target.empty()){
		return ans;
	}
	int nn = target.size();
	for(int i=0;i<nn;i++){
		while(index < target[i]){
			ans.push_back("Push");
			ans.push_back("Pop");
			index++;
		}
		ans.push_back("Push");
		index++;
	}
	return ans;
    }
};
