/*
 * @lc app=leetcode.cn id=852 lang=c
 *
 * [852] 山脉数组的峰顶索引
 */

// @lc code=start
// 时间复杂度为O(N)的方法是，遍历一遍数组，用[i] - [i-1]位置的数字，返回第一个相减为复数的i-1

// 对于O(log(N))的方法是采用二分查找

int peakIndexInMountainArray(int *arr, int arrSize)
{
    int left = 0, right = arrSize - 1, mid;
    while (left < right)
    {
        mid = (left + right) / 2;
        if (arr[mid] - arr[mid -1] > 0  && arr[mid] - arr[mid + 1] > 0)
        {
            break;
        }
        else if (arr[mid] - arr[mid - 1] > 0)
        {
            left = mid;
        }
        else if (arr[mid] - arr[mid + 1] > 0)
        {
            right = mid;
        }
    }
    return mid;
}
// @lc code=end
