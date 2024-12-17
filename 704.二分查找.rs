/*
 * @lc app=leetcode.cn id=704 lang=rust
 * @lcpr version=30204
 *
 * [704] 二分查找
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        if nums.len() < 2 {
            if nums[0] == target {
                return 0;
            } else {
                return -1;
            }
        }

        let mut left: usize = 0;
        let mut right: usize = nums.len() - 1;

        while left <= right {
            let mid = match Self::get_mid(&nums, target, left, right) {
                Some(x) => x,
                None => return -1,
            };
            if nums[mid] == target {
                return mid as i32;
            } else if nums[mid] < target {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    fn get_mid(nums: &Vec<i32>, target: i32, left: usize, right: usize) -> Option<usize> {
        if (target - nums[left]) < 0 {
            return None;
        }

        if (nums[right] - nums[left]) == 0 {
            return Some(left);
        }
        if (target - nums[left]) / (nums[right] - nums[left]) > 1 {
            return None;
        }

        Some(
            ((left as i32)
                + (target - nums[left]) / (nums[right] - nums[left]) * ((right - left) as i32))
                as usize,
        )
    }
}
// @lc code=end

/*
// @lcpr case=start
// [-1,0,3,5,9,12]\n9\n
// @lcpr case=end

// @lcpr case=start
// [-1,0,3,5,9,12]\n2\n
// @lcpr case=end

# @lcpr case=start
# [-1,0,3,5,9,12]\n13\n
# @lcpr case=end

# @lcpr case=start
# [5]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2, 5]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2, 5]\n10\n
# @lcpr case=end


# @lcpr case=start
# [-1,0,5]\n2\n
# @lcpr case=end


# @lcpr case=start
# [-1,0,5]\n0\n
# @lcpr case=end

 */
