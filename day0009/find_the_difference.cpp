class Solution {
public:
    char findTheDifference(string s, string t) {
        
//find the difference


	string alpha = "abcdefghijklmnopqrstuvwxyz";
	
	int as[26] ={0}; 
    int at[26]= {0};
	for(int i=0;i<s.size();i++){
		int tt = s[i] - 97;
		as[tt]++;
	}
	for(int i=0;i<t.size();i++){
		int ty = (int)t[i]-97;
		at[ty]++;
	}  
	int ans;
	for(int i=0;i<26;i++){
		if(as[i]!=at[i]){
			ans =  alpha[i];
			break;
		}
	}
	return ans;
    }
};
