/*
code by : vivek pandey

*/

class MyStack {
public:
    /** Initialize your data structure here. */
    deque<int> q;
    MyStack() {
        
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        q.push_back(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        if(q.empty()){
            return 0;
        }
        int d = q.back();
        q.pop_back();
        return d;
    }
    
    /** Get the top element. */
    int top() {
        return q.back();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        if(q.empty())
            return true;
        return false;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
