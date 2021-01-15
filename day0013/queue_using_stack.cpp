/*
code by : Vivek pandey

*/

class MyQueue {
public:
    /** Initialize your data structure here. */
    stack<int> s,k;
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        s.push(x);
        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if(s.empty()){
            return 0;
        }
        while(!s.empty()){
            k.push(s.top());
            s.pop();
        }
        int df = k.top();
        k.pop();
        while(!k.empty()){
            s.push(k.top());
            k.pop();
        }
        return df;
    }
    
    /** Get the front element. */
    int peek() {
        if(s.empty()){
            return 0;
        }
        stack<int> ss = s;
        stack<int > kk;
        while(!ss.empty()){
            kk.push(ss.top());
            ss.pop();
        }
        int df = kk.top();
         return df;
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        if(s.empty())
            return true;
        return false;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
