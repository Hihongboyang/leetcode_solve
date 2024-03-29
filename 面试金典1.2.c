#include <stdio.h>
#include <stdbool.h>
#include <string.h>

void stringsort(char s[], int star, int end)
{
    // 对字符串进行排序，采用快排
    int temp, low = star, heigh = end;
    if (star < end)
    {
        temp = s[low];
        while (low < heigh)
        {
            while (low < heigh && s[heigh] >= temp)
                heigh--;
            s[low] = s[heigh];

            while (low < heigh && s[low] <= temp)
                low++;
            s[heigh] = s[low];
        }
        s[low] = temp;
        stringsort(s, star, low - 1);
        stringsort(s, low + 1, end);
    }
}

bool doublestringDuplicate(char *s1, char *s2)
{
    // 计算两个字符串是不是相同
    // 先对字符串排序，然后比较两个字符串
    int s_len;
    s_len = strlen(s1);
    if (s_len != strlen(s2))
        return false;

    stringsort(s1, 0, s_len - 1);
    stringsort(s2, 0, s_len - 1);

    while (*s1 != '\0' && *s2 != '\0')
    {
        if (*s1++ != *s2++)
        {
            return false;
        }
    }
    return true;
}

int main(int argc, char const *argv[])
{
    bool count_val;
    char s1[] = "usy";
    char s2[] = "uyk";

    count_val = doublestringDuplicate(s1, s2);
    printf("%d", count_val);
    return 0;
}
