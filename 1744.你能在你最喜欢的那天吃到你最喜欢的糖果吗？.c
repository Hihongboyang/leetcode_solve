/*
 * @lc app=leetcode.cn id=1744 lang=c
 *
 * [1744] 你能在你最喜欢的那天吃到你最喜欢的糖果吗？
 */

// @lc code=start

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

bool *canEat(int *candiesCount, int candiesCountSize, int **queries, int queriesSize, int *queriesColSize, int *returnSize)
{
    int max_candy=0, min_candy=0, max_need=0, min_need=0, i,j;
    bool *answer = (bool *)malloc(sizeof(bool) * (*returnSize));

    for (i = 0; i < queriesSize; i++)
    {
        max_candy = queries[i][1] * queries[i][2];
        min_candy = queries[i][1];

        for (j = 0; j <= queries[i][0]; j++)
        {
            max_need += candiesCount[j];
        }
        min_need = max_need - candiesCount[j-1] + 1;

        if (max_need < min_need || min_need > max_candy)
        {
            *answer = false;
        }
        else
        {
            *answer = true;
        }
        answer++;
        max_need = 0;
        min_need = 0;
    }
    return answer;
}

// int main(int argc, char const *argv[])
// {
//     int *length, len = 3;
//     int first[] = {0,2,2};
//     int sec[] = {4,2,4};
//     int thirt[] = {2,13,1000000000};
//     bool *some;

//     int queries[] = {7,4,5,3,8};

//     int *matrix[3] = {first, sec, thirt};
//     length = &len;

//     some = canEat(queries, 3, matrix, 3, length, length);

//     for (int i = 0; i < 3; i++)
//     {
//         printf("%d ", *some++);
//     }
//     return 0;
// }

// @lc code=end
