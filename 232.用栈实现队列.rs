/*
 * @lc app=leetcode.cn id=232 lang=rust
 * @lcpr version=30204
 *
 * [232] 用栈实现队列
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
struct MyQueue {
    stack_in: Vec<i32>,
    stack_out: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {

    fn new() -> Self {
        MyQueue {
            stack_in: Vec::new(),
            stack_out: Vec::new(),
        }
    }
    
    fn push(&mut self, x: i32) {
        self.stack_in.push(x);
    }
    
    fn pop(&mut self) -> i32 {
        if self.stack_out.is_empty() {
            while !self.stack_in.is_empty() {
                self.stack_out.push(self.stack_in.pop().unwrap());
            }
        }
        self.stack_out.pop().unwrap()
    }
    
    fn peek(&mut self) -> i32 {
        if self.stack_out.is_empty() {
            while !self.stack_in.is_empty() {
                self.stack_out.push(self.stack_in.pop().unwrap());
            }
        }
        *self.stack_out.last().unwrap()
    }
    
    fn empty(&self) -> bool {
        self.stack_in.is_empty() && self.stack_out.is_empty()
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.empty();
 */
// @lc code=end



/*
// @lcpr case=start
// ["MyQueue", "push", "push", "peek", "pop", "empty"][[], [1], [2], [], [], []]\n
// @lcpr case=end

 */

