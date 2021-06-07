#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int sizes[3];
    int stack[90];
    int every_size;
    int numOfStack;
} TripleInOne;


TripleInOne* tripleInOneCreate(int stackSize) {
    TripleInOne *one_stack=malloc(sizeof(TripleInOne));
    one_stack->sizes[0] = 0;
    one_stack->sizes[1] = 0;
    one_stack->sizes[2] = 0;
    one_stack->every_size = stackSize;
    one_stack->numOfStack = 3;
    return one_stack;
}

bool tripleInOneIsEmpty(TripleInOne* obj, int stackNum) {
    if (obj->sizes[stackNum] > 0)
        return false;
    else
        return true;
}

void tripleInOnePush(TripleInOne* obj, int stackNum, int value) {
    if ((obj->sizes[stackNum] >= obj->every_size))
    {
        return;
    }

    
    obj->stack[stackNum*30 + obj->sizes[stackNum]] = value;
    obj->sizes[stackNum]++;
    return;
}

int tripleInOnePop(TripleInOne* obj, int stackNum) {
    if (tripleInOneIsEmpty(obj, stackNum) == true)
    {   
        return -1;
    }
    int ret_val;
    
    obj->sizes[stackNum]--;
    ret_val = obj->stack[stackNum*30 + obj->sizes[stackNum]];
    return ret_val;
}

int tripleInOnePeek(TripleInOne* obj, int stackNum) {
    if(tripleInOneIsEmpty(obj, stackNum) == 1)
    {
        return -1;
    }
    int ret_val;
    ret_val = obj->stack[stackNum*30 + obj->sizes[stackNum]-1];
    return ret_val;
}



void tripleInOneFree(TripleInOne* obj) {
    return;
}

int main(int argc, char const *argv[])
{
    TripleInOne *someone;
    int ret_val;
    someone = tripleInOneCreate(1);
    tripleInOnePush(someone, 0, 1);
    tripleInOnePush(someone, 0, 2);
    ret_val = tripleInOnePop(someone, 0);
    printf("%d ", ret_val);
    ret_val = tripleInOnePop(someone, 0);
    printf("%d ", ret_val);
    ret_val = tripleInOnePop(someone, 0);
    printf("%d ", ret_val);
    ret_val = tripleInOneIsEmpty(someone, 0);
    printf("%d ", ret_val);

    return 0;
}
