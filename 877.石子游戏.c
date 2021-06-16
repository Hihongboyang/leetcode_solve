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

// 看到题解，将数列以位置的奇偶区分，分为第一组和第二组。由于题目说，石子的总数是奇数 没有平局。
// 所以第一组和第二组中，总有一组的和 会比另一组大。而亚历克斯作为第一个选择的人，总是可以选择
// 和大的那一组。
// 5，3，4，5
// 偶 奇 偶 奇
bool stoneGame(int* piles, int pilesSize){
    return true;
}
// @lc code=end

