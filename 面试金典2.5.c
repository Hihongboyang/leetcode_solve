/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdlib.h>
#include <math.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    if (l1 == NULL && l2 == NULL)
        return l1;
    else if (l1 == NULL)
        return l2;
    else if (l2 == NULL)
        return l1;

    int l1_val, l2_val;
    struct ListNode *new_head = malloc(sizeof(struct ListNode)), *head;
    head = new_head;

    div_t divmod;
    int quot = 0;
    while (l1 != NULL || l2 != NULL)
    {
        // 只要还有一个列表没有完成就继续
        struct ListNode *temp = malloc(sizeof(struct ListNode));
        l1_val = (l1 == NULL) ? 0 : l1->val; // 保证两个链表总有值
        l2_val = (l2 == NULL) ? 0 : l2->val;

        divmod = div(l1_val + l2_val + quot, 10);
        quot = divmod.quot;
        temp->val = divmod.rem;  // 将余数给新链表
        temp->next = NULL;
        head->next = temp;
        head = temp;

        l1 = (l1 == NULL) ? NULL : l1->next;
        l2 = (l2 == NULL) ? NULL : l2->next;
    }
    if (quot)
    {
        // 判断最后有没有进位
        struct ListNode *temp = malloc(sizeof(struct ListNode));
        temp->val = quot;
        temp->next = NULL;
        head->next = temp;
    }
    return new_head->next;
}