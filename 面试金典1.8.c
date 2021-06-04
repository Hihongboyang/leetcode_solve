#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。 */

void setZeroes(int **matrix, int matrixSize, int *matrixColSize)
{
    if (matrixSize < 2 && *matrixColSize < 2)
        return;
    
    // 先统计矩阵中0的位置，让后将对应行列置为0
    int row_record[matrixSize * (*matrixColSize)], col_record[matrixSize * (*matrixColSize)], *pr, *pc;

    memset(row_record, -1, sizeof(int) * matrixSize * (*matrixColSize));
    memset(col_record, -1, sizeof(int) * matrixSize * (*matrixColSize));
    pr = row_record;
    pc = col_record;

    for (int i = 0; i < matrixSize; i++)
    {
        for (int j = 0; j < *matrixColSize; j++)
        {
            if (matrix[i][j] == 0)
            {
                *pr++ = i;
                *pc++ = j;
            }
        }
    }

    pr = row_record;
    pc = col_record;

    while (*pr != -1)
    {
        memset(matrix[*pr], 0, sizeof(int) * (*matrixColSize));
        pr++;
    }

    while (*pc != -1)
    {
        for (int i = 0; i < matrixSize; i++)
        {
            matrix[i][*pc] = 0;
        }
        pc++;
    }
}

int main(int argc, char const *argv[])
{
    int *length, len = 3;
    int first[] = {1, 2, 3};
    int sec[] = {4, 5, 0};
    int thirt[] = {7, 8, 9};

    int *matrix[3] = {first, sec, thirt};
    length = &len;

    setZeroes(matrix, 3, length);

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
    return 0;
}
