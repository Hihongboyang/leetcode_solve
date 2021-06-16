/*
 * @lc app=leetcode.cn id=877 lang=c
 *
 * [877] 石子游戏
 */

// @lc code=start

#include <stdlib.h>
#include <stdbool.h>

// 按照题目的意思是只有 亚历克斯无论如何都应赢不了的时候才返回false
// 那么亚历克斯 每次都取最大的数， 而李每次都取最小的数，如果这样亚历克斯都
// 赢不了，那么就返回false。但是感觉这样有问题。
bool stoneGame(int* piles, int pilesSize){
    int left = 0, right = pilesSize - 1, ya = 0, li = 0;
    for (int i = 0; i<pilesSize; i++)
    {
        if(i % 2 == 0)
        {
            if (piles[left] > piles[right])
            {
                ya += piles[left];
                left++;
            }
            else
            {
                ya += piles[right];
                right--;
            }
        }
        else
        {
            if (piles[left] < piles[right])
            {
                li += piles[left];
                left++;
            }
            else
            {
                li += piles[right];
                right--;
            }
        }
    }
    return ya > li;
}
// @lc code=end

