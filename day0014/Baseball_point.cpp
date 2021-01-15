/* code by : vivek pandey 

*/

class Solution {
public:
    int calPoints(vector<string>& ops) {
        

//Baseball Game

	stack <int> ans;  //making a stack
	 
	for(auto i:ops){
		if(i=="+"){   //checking for every condition
			int a = ans.top();
			ans.pop();
			int b = ans.top() + a;
			ans.push(a);
			ans.push(b);
		}
		else if(i=="C"){
			ans.pop();
		}
		else if(i=="D"){
			ans.push(2*ans.top());
		}
		else{
            int t =  stoi(i); //converting string number as it is in intger
			ans.push(t);
		}
		
	}
	
	int ret=0;  ///finding the submission (addition)
	while(!ans.empty()){
		ret += ans.top();
		ans.pop();
	}
	return ret; //finally returing the all
    }
};
