#include <string.h>
#include <stdbool.h>
#include <stdio.h>

bool canPermutePalindrome(char *s)
{
    int mapping[128] = {0}, len = strlen(s), sum=0;
    char *p = s;
    while (*p != '\0')
    {
        mapping[*p++]++;
    }

    for (int i = 0; i < 128; i++)
    {
        if (mapping[i] % 2 == 1)
            sum++;
        if (sum > 1)
            return false;
    }
    return true;
}

int main(int argc, char const *argv[])
{
    //给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
    // 回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。回文串不一定是字典当中的单词

    char S[] = "abcde";
    bool som;

    som = canPermutePalindrome(S);
    printf("%d\n", som);
    return 0;
}
