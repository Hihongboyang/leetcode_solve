#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>

char *compressString(char *S)
{
    int len_str, cont_val = 0, site;
    div_t divmod;
    char *str_p = S, char_val, *ret_char, *p3;

    len_str = strlen(S);
    if (len_str < 2)
        return S;

    if ((ret_char = malloc(2 * len_str * sizeof(char))) == NULL)
        return false;
    p3 = ret_char;

    char_val = str_p[0];
    while (*str_p != '\0')
    {
        if (*str_p == char_val)
        {
            cont_val++;
        }
        else
        {
            *p3++ = char_val;
            site = (int)log10(cont_val);

            p3 += site;
            divmod = div(cont_val, 10);

            while (site >= 0)
            {
                *p3-- = divmod.rem + '0';
                divmod = div(divmod.quot, 10);
                site--;
            }
            p3 = p3 + (int)(log10(cont_val) + 2);
            char_val = *str_p;
            cont_val = 1;
        }
        str_p++;
    }
    *p3++ = char_val;

    site = (int)log10(cont_val);
    p3 += site;
    divmod = div(cont_val, 10);
    while (site >= 0)
    {
        *p3-- = divmod.rem + '0';
        divmod = div(divmod.quot, 10);
        site--;
    }
    // *p3++ = divmod.rem + '0';
    p3 = p3 + (int)(log10(cont_val) + 2);
    *p3 = '\0';


    return strlen(ret_char) < len_str ? ret_char : S;
}

int main(int argc, char const *argv[])
{
    char *first = "aabcccccaa";
    char *value;
    value = compressString(first);
    printf("%s\n", value);
    return 0;
}
