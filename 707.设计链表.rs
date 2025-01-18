/*
 * @lc app=leetcode.cn id=707 lang=rust
 * @lcpr version=30204
 *
 * [707] 设计链表
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

struct MyLinkedList {
    size: usize,
    head: Option<Box<Node>>
}

struct Node {
    val: i32,
    next: Option<Box<Node>>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyLinkedList {

    fn new() -> Self {
        MyLinkedList {
            size: 0,
            head: None,
        }
    }
    
    fn get(&self, index: i32) -> i32 {
        if index < 0{
            return -1;
        }
        let mut i = 0;
        let mut current = &self.head;

        while let Some(node) = current {
            if i == index {
                return node.val;
            }
            i += 1;
            current = &node.next;
        }
        return -1;
    }
    
    fn add_at_head(&mut self, val: i32) {
        let node = Box::new(Node {
            val: val,
            next: self.head.take(),
        });
        self.head = Some(node);
        self.size += 1;
    }
    
    fn add_at_tail(&mut self, val: i32) {
        let mut current = &mut self.head;

        while let Some(node) = current {
            current = &mut node.next;
        }
        *current = Some(Box::new(Node {
            val, 
            next: None,
        }));
    }
    
    fn add_at_index(&mut self, index: i32, val: i32) {
        if index <= 0 {
            self.add_at_head(val);
        }

        let mut i = 0;
        let mut current = &mut self.head;

        while let Some(node) = current {
            if i + 1 == index {
                node.next = Some(Box::new(Node {
                    val, 
                    next: node.next.take(),
                }));
                return;
            } else {
                i += 1;
                current = &mut node.next;
            }
        }
    }
    
    fn delete_at_index(&mut self, index: i32) {
        if index < 0 {
            return;
        }
        let mut i = 0;
        let mut current = self;
        while let Some(ref mut node) = current.next {
            if i == index {
                current.next = node.next.take();
                break;
            }
            i += 1;
            current = current.next.as_mut().unwrap();
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * let obj = MyLinkedList::new();
 * let ret_1: i32 = obj.get(index);
 * obj.add_at_head(val);
 * obj.add_at_tail(val);
 * obj.add_at_index(index, val);
 * obj.delete_at_index(index);
 */
// @lc code=end



