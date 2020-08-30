/*
code by : vivek pandey

*/

class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> s;
    deque<int> q;
    
    MinStack() {
        
    }
    
    void push(int x) {
        s.push(x);
        if(x>q.front()){
            q.push_back(x);
        }    
        else{
            q.push_front(x);
        }
    }
    
    void pop() {
        if(s.top()==q.front()){
            q.pop_front();
        }
        else{
            q.pop_back();
        }
        s.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return q.front();
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
