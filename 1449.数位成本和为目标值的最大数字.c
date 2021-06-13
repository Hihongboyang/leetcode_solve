/*
 * @lc app=leetcode.cn id=1449 lang=c
 *
 * [1449] 数位成本和为目标值的最大数字
 */

// @lc code=start


char* largestNumber(int* cost, int costSize, int target) {
    int dp[target + 1];
    memset(dp, 0x80, sizeof(dp));
    dp[0] = 0;
    for (int i = 0; i < costSize; ++i) {
        for (int j = cost[i]; j <= target; ++j) {
            dp[j] = fmax(dp[j], dp[j - cost[i]] + 1);
        }
    }
    if (dp[target] < 0) {
        return "0";
    }
    char* ans = malloc(sizeof(char) * (target + 1));
    int ansSize = 0;
    for (int i = 8, j = target; i >= 0; i--) {
        for (int c = cost[i]; j >= c && dp[j] == dp[j - c] + 1; j -= c) {
            ans[ansSize++] = '1' + i;
        }
    }
    ans[ansSize] = 0;
    return ans;
}
// @lc code=end

