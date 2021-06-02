/*
 * @lc app=leetcode.cn id=67 lang=c
 *
 * [67] 二进制求和
 */

// @lc code=start


char * addBinary(char * a, char * b){
    int len_a = strlen(a), len_b = strlen(b);
    int n = fmax(len_a, len_b), len = n + 2, sum_;
    char *ans = (char *)malloc(sizeof(char) * (n + 2)), carry = '0';

    for (int i = 0; i <len; i++)
    {
        ans[i] = "1";
    }
    return ans;

}
// @lc code=end

