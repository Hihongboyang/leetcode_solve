#include <stdlib.h>
#include <stdio.h>

typedef struct element_{
    int number;
    struct element_ *next;
} Element;

typedef struct {
    Element *cat_head;
    Element *cat_tail;

    Element *dog_head;
    Element *dog_tail;
    int size;
} AnimalShelf;


AnimalShelf* animalShelfCreate() {
    AnimalShelf *queue = (AnimalShelf *)malloc(sizeof(AnimalShelf));
    Element *cat_que = (Element *)malloc(sizeof(Element));
    Element *dog_que = (Element *)malloc(sizeof(Element));

    cat_que->next = NULL;
    cat_que->number = -1;

    dog_que->next = NULL;
    dog_que->number = -1;

    queue->cat_head = cat_que;
    queue->cat_tail = cat_que;

    queue->dog_head = dog_que;
    queue->dog_tail = dog_que;
    queue->size = 20000;

    return queue;
}

void animalShelfEnqueue(AnimalShelf* obj, int* animal, int animalSize) {
    if (obj == NULL)
    {
        return;
    }
    
    Element *temp = (Element *)malloc(sizeof(Element)); // create new element
    temp->number = animal[0];  // animal number
    temp->next = NULL;
    // tail insert
    if (animal[1] == 0)
    {
        // cat
        obj->cat_tail->next = temp;
        obj->cat_tail = temp;
    }
    else
    {
        // dog
        obj->dog_tail->next = temp;
        obj->dog_tail = temp;
    }
    obj->size--;
    return;
}


int* animalShelfDequeueDog(AnimalShelf* obj, int* retSize) {
    *retSize = 2;
    int *ret = (int *)malloc(sizeof(int) * 2);


    if (obj == NULL || obj->dog_head->next == NULL)
    {
        ret[0] = -1;
        ret[1] = -1;

        return ret;
    }

    ret[0] = obj->dog_head->next->number;
    ret[1] = 1;

    obj->dog_head->next = obj->dog_head->next->next;
    obj->size++;

    if (obj->dog_head->next == NULL)
    {
        obj->dog_tail = obj->dog_head;
    }
    return ret;
}

int* animalShelfDequeueCat(AnimalShelf* obj, int* retSize) {
    *retSize = 2;
    int *ret = (int *)malloc(sizeof(int) * 2);

    if (obj == NULL || obj->cat_head->next == NULL)
    {
        ret[0] = -1;
        ret[1] = -1;
        return ret;
    }

    ret[0] = obj->cat_head->next->number;
    ret[1] = 0;

    obj->cat_head->next = obj->cat_head->next->next;
    obj->size++;

    if (obj->cat_head->next == NULL)
    {
        obj->cat_tail = obj->cat_head;
    }
    return ret;
}


int* animalShelfDequeueAny(AnimalShelf* obj, int* retSize) {
    *retSize = 2;
    int *ret = (int *)malloc(sizeof(int) * 2);

    if (obj->cat_head->next == NULL)
    {
        ret = animalShelfDequeueDog(obj, retSize);
    }
    else if (obj->dog_head->next == NULL)
    {
        ret = animalShelfDequeueCat(obj, retSize);
    }
    else if ((obj->cat_head->next->number) < (obj->dog_head->next->number))
    {
        ret = animalShelfDequeueCat(obj, retSize);
    }
    else if ((obj->cat_head->next->number) > (obj->dog_head->next->number))
    {
        ret = animalShelfDequeueDog(obj, retSize);
    }
    else
    {
        ret[0] = -1;
        ret[1] = -1;
    }
    return ret;
}
    
void animalShelfFree(AnimalShelf* obj) {
    if (obj == NULL)
    {
        return;
    }

    free(obj->cat_head);
    free(obj->dog_head);
    free(obj);
}