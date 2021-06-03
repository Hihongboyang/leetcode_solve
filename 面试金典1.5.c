#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

bool oneEditAway(char *first, char *second)
{
    // 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

    int diff = 0, sum1 = 0;
    char *short_p, *long_p;

    diff = strlen(first) - strlen(second);
    if (diff > 1 || diff < -1)
    {
        return false;
    }

    if (diff > 0)
    {
        short_p = second;
        long_p = first;
    }
    else
    {
        short_p = first;
        long_p = second;
    }

    while (*short_p != '\0')
    {
        // 比较两个字符串，如果不一样，长的指针加一
        if (*short_p != *long_p)
        {
            sum1++;
            if (sum1 > 1)
            {
                return false;
            }
            if (diff != 0)
            {
                long_p++;
                continue;
            }
        }

        short_p++;
        long_p++;
    }
    return true;
}

int main(int argc, char const *argv[])
{

    char first[] = "horse", second[] = "rohse";
    bool som;

    som = oneEditAway(first, second);
    printf("%d\n", som);
    return 0;
}
