#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

/*字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。*/

bool isFlipedString(char* s1, char* s2){
    // 将s2复制一遍， s1就在s2当中
    size_t s1_len, s2_len;
    char *all_str;
    s1_len = strlen(s1);
    s2_len = strlen(s2);
    if (s1_len != s2_len)
    {
        return false;
    }
    if (strcmp(s1, s2) == 0)
    {
        return true;
    }

    all_str = calloc(s1_len * 2 + 1, sizeof(char));
    strcat(all_str, s2);
    strcat(all_str, s2);

    if (strstr(all_str, s1) == NULL)
    {
        return false;
    }    
    else
    {
        return true;
    }

}

int main(int argc, char const *argv[])
{
    char *s1 = "eeelee", *s2 = "eeeeel";
    bool some;
    some = isFlipedString(s1, s2);
    printf("%d", some);

    return 0;
}