/*
**********auther- Anand Keshari********************
problem link -https://leetcode.com/problems/min-stack/
*/

class MinStack {
public:
    /** initialize your data structure here. */
        vector<int> stack;
        vector<int> min;
    void push(int x) {
        if(stack.empty() || x<min[min.size()-1])
        {
            min.push_back(x);
        }
        else
        {
            min.push_back(min[min.size()-1]);
        }
        stack.push_back(x);
    }
    
    void pop() {
        stack.pop_back();
        min.pop_back();
    }
    
    int top() {
        return stack[stack.size()-1]; 
    }
    
    int getMin() {
        return min[min.size()-1];
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
