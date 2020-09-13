/* Code by : Vivek Pandey

Approach : Greedy

*/


class Solution {
public:
    int largestSumAfterKNegations(vector<int>& a, int k) {
            ///

	sort(a.begin(),a.end());
	int cntneg=0;
	int n = a.size();
	for(int i=0;i<n;i++){
		if(a[i]<0){
			cntneg++;
		}
		else{
			break;
		}
	}
	
	if(cntneg==0){
		if(k%2){
			a[0] = a[0]*(-1);
		}
	}
	
	else{
		int i=0;
		while(cntneg && i<n-1  && k){
			if(a[i]<0){
				a[i] = a[i] * (-1);
				i++;
                k--;
                cntneg--;
			}
			else{
				break;
			}
		}
		if(k){
			if(i==0 || i<n-1){
				if(k%2){
					a[i] = a[i] * (-1);
				}
			}
			else{
				if(abs(a[i])>a[i+1]){
					if(k%2){
					a[i+1] = a[i+1] * (-1);
					}	
				}
				else{
					if(k%2){
					a[i] = a[i] * (-1);
					}		
				}
			}
		}
	}
	int sum=0;
	for(int j=0;j<n;j++){
		sum += a[j];
	}
	return sum;
    }
};
