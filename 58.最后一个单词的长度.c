/*
 * @lc app=leetcode.cn id=58 lang=c
 *
 * [58] 最后一个单词的长度
 */

// @lc code=start

int lengthOfLastWord(char *s)
{
    char *p;
    p = s;
    int pre_count=0, count=0;
    while(*p !='\0')
    {
        if (*p != ' ')
            count++;
        else
        {   
            if (count > 0)
                pre_count = count;
            count = 0;
        }
        p++;
    }
    if (count > 0)
        pre_count = count;

    return pre_count;
}
// @lc code=end
