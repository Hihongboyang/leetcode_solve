/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* partition(struct ListNode* head, int x){
    struct ListNode *new_element = malloc(sizeof(struct ListNode)), *new_head, *new_tail;
    new_head = new_element;
    new_tail = new_element;
    new_element->val = head->val;
    new_element->next = NULL;
    head = head->next;

    while(head != NULL)
    {
        struct ListNode *temp = malloc(sizeof(struct ListNode));
        temp->val = head->val;
        temp->next = NULL;
        if (head->val < x)
        {
            // 头插法
            temp->next = new_head;
            new_head = temp;
        }
        else
        {
            // 尾插法
            new_tail->next = temp;
            new_tail = temp;
        }
        head = head->next;
    }
    return new_head;
}