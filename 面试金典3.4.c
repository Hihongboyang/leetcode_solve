#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct
{
    int size;
    int push_point;
    int pop_point;

    int *push_value;
    int *pop_value;
} MyQueue;

/** Initialize your data structure here. */

MyQueue *myQueueCreate()
{
    MyQueue *queue = (MyQueue *)malloc(sizeof(MyQueue));
    int *push = (int *)malloc(sizeof(int) * 100);
    int *pop = (int *)malloc(sizeof(int) * 100);

    queue->pop_point = 0;
    queue->push_point = 0;
    queue->pop_value = pop;
    queue->push_value = push;
    queue->size = 100;

    return queue;
}

/** Push element x to the back of queue. */
void myQueuePush(MyQueue *obj, int x)
{
    if (obj == NULL)
    {
        return;
    }
    if (obj->push_point == obj->size)
    {
        return;
    }
    obj->push_value[obj->push_point] = x;
    obj->push_point++;
}

/** Removes the element from in front of queue and returns that element. */
int myQueuePop(MyQueue *obj)
{
    if (obj == NULL)
    {
        return -1;
    }
    int ret_val;
    if (obj->pop_point >= 1)
    {
        ret_val = obj->pop_value[obj->pop_point - 1];
        obj->pop_point--;
    }

    else if (obj->pop_point == 0 && obj->push_point >= 1)
    {
        while (obj->push_point >= 1)
        {
            obj->pop_value[obj->pop_point] = obj->push_value[obj->push_point - 1];
            obj->pop_point++;
            obj->push_point--;
        }
        ret_val = obj->pop_value[obj->pop_point - 1];
        obj->pop_point--;
    }
    else
    {
        return -1;
    }
    return ret_val;
}

/** Get the front element. */
int myQueuePeek(MyQueue *obj)
{
    if (obj == NULL)
    {
        return -1;
    }
    int ret_val;

    if (obj->pop_point < 1)
    {
        if (obj->push_point < 1)
        {
            return -1;
        }
        ret_val = obj->push_value[0];
    }
    else
    {
        ret_val = obj->pop_value[obj->pop_point - 1];
    }

    return ret_val;
}

/** Returns whether the queue is empty. */
bool myQueueEmpty(MyQueue *obj)
{
    return (obj->pop_point < 1) && (obj->push_point < 1);
}

void myQueueFree(MyQueue *obj)
{
    free(obj->pop_value);
    free(obj->push_value);
    free(obj);
}

int main(int argc, char const *argv[])
{
    // 使用两个列表完成一个队列
    MyQueue *queue;
    int val;
    queue = myQueueCreate();

    myQueuePush(queue, -2);
    myQueuePush(queue, 0);
    myQueuePush(queue, -1);

    printf("%d ", myQueuePeek(queue));
    printf("%d ", myQueuePop(queue));
    printf("%d ", myQueuePeek(queue));

    myQueuePush(queue, 4);
    myQueuePush(queue, 5);
    myQueuePush(queue, 66);
    printf("%d ", myQueuePop(queue));
    printf("%d ", myQueuePop(queue));
    printf("%d ", myQueuePop(queue));
    printf("%d ", myQueueEmpty(queue));
    printf("%d ", myQueuePop(queue));
    printf("%d ", myQueuePop(queue));
    printf("%d ", myQueueEmpty(queue));

    return 0;
}