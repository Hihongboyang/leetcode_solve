/*
 * @lc app=leetcode.cn id=225 lang=rust
 * @lcpr version=30204
 *
 * [225] 用队列实现栈
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
struct MyStack {
    queue: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyStack {

    fn new() -> Self {
        MyStack { queue: Vec::new() }
    }
    
    fn push(&mut self, x: i32) {
        self.queue.push(x);
    }
    
    fn pop(&mut self) -> i32 {
        let len = self.queue.len() - 1;
        for _ in 0..len {
            let tmp = self.queue.remove(0);
            self.queue.push(tmp);
        }
        self.queue.remove(0)
    }
    
    fn top(&mut self) -> i32 {
        let res = self.pop();
        self.queue.push(res);
        res
    }
    
    fn empty(&self) -> bool {
        self.queue.is_empty()
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * let obj = MyStack::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: bool = obj.empty();
 */
// @lc code=end



/*
// @lcpr case=start
// ["MyStack", "push", "push", "top", "pop", "empty"][[], [1], [2], [], [], []]\n
// @lcpr case=end

 */

