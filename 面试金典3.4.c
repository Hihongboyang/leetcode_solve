#include <stdlib.h>
#include <stdio.h>

typedef struct Element_
{
    int point;  // 存储当栈中数据的位置
    int order;  // 标记当前为第几个栈
    int *value; // 使用数组存储数据
    struct Element_ *next;
    struct Element_ *pre;
} Stack_Element;

typedef struct StackOfPlates_
{
    int size; // 保存每个栈的大小
    Stack_Element *head;
    Stack_Element *tail;

} StackOfPlates;

StackOfPlates *stackOfPlatesCreate(int cap)
{
    StackOfPlates *stack = (StackOfPlates *)malloc(sizeof(StackOfPlates));
    Stack_Element *element = (Stack_Element *)malloc(sizeof(Stack_Element));
    int *list = cap > 0 ? (int *)malloc(sizeof(int) * cap) : NULL;
    element->value = list;
    element->point = 0;
    element->next = NULL;
    element->pre = NULL;
    element->order = 0;

    stack->size = cap;
    stack->head = element;
    stack->tail = element;
    return stack;
}

void stackOfPlatesPush(StackOfPlates *obj, int val)
{
    if (obj->size < 1)
    {
        return;
    }
    if (obj->tail == NULL || obj->tail->point >= obj->size)
    {
        Stack_Element *element = (Stack_Element *)malloc(sizeof(Stack_Element));
        int *list = obj->size > 0 ? (int *)malloc(sizeof(int) * obj->size) : NULL;
        list[0] = val;
        element->value = list;
        element->point = 1;
        element->next = NULL;
        if (obj->tail == NULL)
        {
            element->order = 0;
        }
        else
        {
            element->order = obj->tail->order + 1;
        }

        element->pre = obj->tail;
        if (obj->tail != NULL)
            obj->tail->next = element;
        obj->tail = element;
        if (obj->head == NULL)
        {
            obj->head = element;
        }
    }
    else
    {
        obj->tail->value[obj->tail->point] = val;
        obj->tail->point++;
    }
}

int stackOfPlatesPop(StackOfPlates *obj)
{
    int ret_val;
    if (obj->tail == NULL || obj->size < 1)
    {
        return -1;
    }

    if (obj->tail->point >= 1)
    {
        ret_val = obj->tail->value[obj->tail->point - 1];
        obj->tail->point--;
        if (obj->tail->point == 0 && obj->tail->order != 0) // 检查是不是第一个栈，保证总有一个栈存在。
        {
            obj->tail = obj->tail->pre;
            obj->tail->next = NULL;
        }
    }
    else
    {
        ret_val = -1;
    }
    return ret_val;
}

int stackOfPlatesPopAt(StackOfPlates *obj, int index)
{
    int ret_val;
    Stack_Element *p = obj->head;
    

    while (p != NULL && p->order != index)
    {
        // 寻找index的位置
        p = p->next;
    }
    if (p == NULL || obj->size < 1)
    {
        // index超出了当前栈数量
        return -1;
    }

    // 找到对应的栈了，
    if (p->point >= 1)
    {
        ret_val = p->value[p->point - 1];
        p->point--;
        if (p->point == 0 && p->order != 0) // 检查是不是第一个栈，保证总有一个栈存在。
        {
            p->pre->next = p->next;
            if (p->next != NULL)
            {
                p->next->order--;
                p->next->pre = p->pre;
            }
            else
            {
                obj->tail = p->pre;
            }
        }
    }
    else
    {
        ret_val = stackOfPlatesPop(obj);
    }

    return ret_val;
}

void stackOfPlatesFree(StackOfPlates *obj)
{
    free(obj);
}

int main(int argc, char const *argv[])
{
    // 内存消耗较少，但是耗时较长。使用，数组的化耗时应该会下降。
    StackOfPlates *stack;
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
