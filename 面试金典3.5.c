#include <stdlib.h>
#include <stdbool.h>

typedef struct
{
    int point;
    int *stack;

} SortedStack;

SortedStack *sortedStackCreate()
{
    SortedStack *stack = (SortedStack *)malloc(sizeof(SortedStack));
    int *temp = (int *)malloc(sizeof(int) * 5000);
    stack->stack = temp;
    stack->point = 0;
    return stack;
}

void sortedStackPush(SortedStack *obj, int val)
{
    int *temp_stack = (int *)malloc(sizeof(int) * 5000);
    int temp = 0, temp_point = 0;
    while(obj->point >= 1)
    {
        temp = obj->stack[obj->point - 1];
        obj->point--;

        if (temp < val)
        {
            temp_stack[temp_point] = temp;
            temp_point++;
        }
        else
        {
            obj->stack[obj->point] = temp;
            obj->point++;
            break;
        }        
    }
    obj->stack[obj->point] = val;
    obj->point++;
    while(temp_point >= 1)
    {
        obj->stack[obj->point] = temp_stack[temp_point - 1];
        obj->point++;
        temp_point--;
    }
    return;
}

void sortedStackPop(SortedStack *obj)
{
    if (obj->point >= 1)
    {
        obj->point--;
    }
    return;
}

int sortedStackPeek(SortedStack *obj)
{
    int ret_val = -1;

    if (obj->point >= 1)
    {
        ret_val = obj->stack[obj->point - 1];
    }
    return ret_val;
}

bool sortedStackIsEmpty(SortedStack *obj)
{
    return obj->point >= 1;
}

void sortedStackFree(SortedStack *obj)
{
    free(obj->stack);
    free(obj);
}

int main(int argc, char const *argv[])
{
    // 内存消耗较少，但是耗时较长。使用，数组的化耗时应该会下降。
    SortedStack *stack;
    int val;
    stack = stackOfPlatesCreate(2);

    stackOfPlatesPush(stack, -2);
    stackOfPlatesPush(stack, 0);
    stackOfPlatesPush(stack, -1);

    val = stackOfPlatesPop(stack);
    printf("%d ", val);
    val = stackOfPlatesPopAt(stack, 0);
    printf("%d ", val);
    val = stackOfPlatesPop(stack);
    printf("%d ", val);
    return 0;
}
