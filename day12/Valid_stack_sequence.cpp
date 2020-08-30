/*
code by: Vivek pandey

*/


class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> pus;
        stack<int> pob;
        while(!popped.empty()){
            pob.push(popped.back());
            popped.pop_back();
        }
        for(int i=0;i<pushed.size();i++){
            pus.push(pushed[i]);
            if(pus.top()==pob.top()){
                while(!pus.empty() && !pob.empty() && pob.top()==pus.top()){
                    pus.pop();
                    pob.pop();
                }
            }
        }
        if(!pus.empty() || !pob.empty()){
            return false;
        }
        return true;
    }
};
