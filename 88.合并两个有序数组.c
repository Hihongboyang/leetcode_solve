/*
 * @lc app=leetcode.cn id=88 lang=c
 *
 * [88] 合并两个有序数组
 */

// @lc code=start

void merge(int *nums1, int nums1Size, int m, int *nums2, int nums2Size, int n)
{
    int p1 = m - 1, p2 = n - 1, tail = nums1Size-1,i;

    while (p1 >= 0 && p2 >= 0)
    {
        if (nums1[p1] > nums2[p2])
        {
            nums1[tail] = nums1[p1];
            p1--;
            tail--;
        }
        else
        {
            nums1[tail] = nums2[p2];
            p2--;
            tail--;
        }
    }
    while (p1 >= 0)
    {
        nums1[tail] = nums1[p1];
        p1--;
        tail--;
    }
    while (p2 >= 0)
    {
        nums1[tail] = nums2[p2];
        p2--;
        tail--;
    }
}
// @lc code=end
