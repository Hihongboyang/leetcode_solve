/*
 * @lc app=leetcode.cn id=278 lang=c
 *
 * [278] 第一个错误的版本
 */

// @lc code=start
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    int left = 1, right = n, mid;
    

    while (left < right)
    {
        mid = left + (right - left) / 2; // 防止溢出
        if (isBadVersion(mid) == false)
        {
            left = mid + 1;
        }
        else
        {
            right = mid;
        }
    }
    return left;
    
}
// @lc code=end

