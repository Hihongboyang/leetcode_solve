/* 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。
请你设计一种算法，将图像旋转 90 度。不占用额外内存空间能否做到？*/
#include <stdio.h>
#include <stdlib.h>
int swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void rotate(int **matrix, int matrixSize, int *matrixColSize)
{
    int *temp;
    // 对矩阵进行 行互换
    for (int j = 0; j < matrixSize/2; j++)
    {
        temp = matrix[j];
        matrix[j] = matrix[matrixSize-1 - j];
        matrix[matrixSize-1 - j] = temp;
    }

    // 对矩阵进行主对角元素变换
    for (int i = 0; i < matrixSize; i++)
    {
        for (int j = 0; j < i; j++)
        {
            swap(&matrix[i][j], &matrix[j][i]);
        }
    }
}

int main(int argc, char const *argv[])
{
    int *length, len = 3;
    int first[] = {1, 2, 3};
    int sec[] = {4, 5, 6};
    int thirt[] = {7, 8, 9};

    int *matrix[3] = {first, sec, thirt};
    length = &len;

    rotate(matrix, 3, length);

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
