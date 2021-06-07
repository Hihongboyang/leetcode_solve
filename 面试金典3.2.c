#include <stdlib.h>
#include <limits.h>

typedef struct element_
{
    int val;
    struct element_ *next;
}Element;

typedef struct
{
    int size;
    Element *head;
    Element *tail;
    Element *head_min;
    Element *tail_min;

} MinStack;

#define stack_size(stack) ((stack)->size)

/** initialize your data structure here. */

MinStack *minStackCreate()
{
    MinStack *stack = (MinStack *)malloc(sizeof(MinStack));
    Element *new_element = (Element *)malloc(sizeof(Element));
    Element *new_element_min = (Element *)malloc(sizeof(Element));
    new_element->val = -1;
    new_element->next = NULL;

    new_element_min->val = INT_MAX;
    new_element_min->next = NULL;

    stack->size = 0;
    stack->head = new_element;
    stack->head_min = new_element_min;
    stack->tail = new_element;
    stack->tail_min = new_element_min;
    return stack;
}

void minStackPush(MinStack *obj, int x)
{
    Element *new_element = (Element *)malloc(sizeof(Element));
    Element *new_element_min = (Element *)malloc(sizeof(Element));

    // 头插法
    new_element->val = x;
    new_element->next = obj->head;
    obj->head = new_element;
    obj->size++;

    new_element_min->val = (x < obj->head_min->val) ? x: obj->head_min->val;
    new_element_min->next = obj->head_min;
    obj->head_min = new_element_min;
}

void minStackPop(MinStack *obj)
{
    if (stack_size(obj) == 0)
    {
        return;
    }

    Element *temp;
    temp = obj->head;
    obj->head = obj->head->next;
    free(temp);

    temp = obj->head_min;
    obj->head_min = obj->head_min->next;
    free(temp);
    obj->size--;
}

int minStackTop(MinStack *obj)
{
    if (stack_size(obj) == 0)
    {
        return -1;
    }
    return obj->head->val;
}

int minStackGetMin(MinStack *obj)
{
    if (stack_size(obj) == 0)
    {
        return -1;
    }

    return obj->head_min->val;
}

void minStackFree(MinStack *obj)
{
    free(obj);
}


int main(int argc, char const *argv[])
{

    MinStack *stack;
    int val;
    stack = minStackCreate();

    minStackPush(stack, -2);
    minStackPush(stack, 0);
    minStackPush(stack, -1);

    val = minStackGetMin(stack);
    printf("%d ", val);
    minStackTop(stack);
    minStackTop(stack);
    val = minStackGetMin(stack);
    printf("%d ", val);
    return 0;
}
