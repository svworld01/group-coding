/* code by :  Vivek pandey
*/

Solution



class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(),people.end());
        int n = people.size()-1;
        
        int i=0;
        
        int ant=0;
        while(i<=n){
            if(people[i] + people[n]<=limit){
                i++;
               n--;
            }
            else{
                n--;
            }
            ant++;
        }
        return ant;
    }
};
