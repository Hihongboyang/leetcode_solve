/*
 * @lc app=leetcode.cn id=13 lang=c
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
int mapping_s(char key)
{
    int value;
    switch (key)
    {
    case 'I':
        value = 1;
        break;
    case 'V':
        value = 5;
        break;
    case 'X':
        value = 10;
        break;
    case 'L':
        value = 50;
        break;
    case 'C':
        value = 100;
        break;
    case 'D':
        value = 500;
        break;
    case 'M':
        value = 1000;
        break;
    }
    return value;
}

int romanToInt(char *s){
    int sum=0, length = strlen(s);
    char stack=s[0];
    sum += mapping_s(s[0]);

    for(int i=1; i < length; i++)
    {
        if(mapping_s(s[i]) > mapping_s(stack))
        {
            sum = sum - mapping_s(stack) * 2 + mapping_s(s[i]);
        }
        else
        {
            sum += mapping_s(s[i]);
        }
        stack = s[i];
    }
    return sum;

}
// @lc code=end

