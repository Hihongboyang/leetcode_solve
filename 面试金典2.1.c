/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* removeDuplicateNodes(struct ListNode* head){
    if (head == NULL)
    {
        return head;
    }
    int mapping[20000] = {0}, is_exists;
    struct ListNode *p_head=head, *before;

    while(p_head != NULL)
    {
        is_exists = mapping[p_head->val];
        if (is_exists != 0)
        {
            before->next = p_head->next;
        }
        else
        {
            mapping[p_head->val] = 1;
            before = p_head;
        }
        p_head = p_head->next;
    }
    return head;
}