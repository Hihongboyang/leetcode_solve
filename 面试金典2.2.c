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

struct ListNode
{
    int val;
    struct ListNode *next;
};
/* 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。 */
// 双指针，第一个指针先移动k个位置，然后两个指针一起移动。
int kthToLast(struct ListNode *head, int k)
{
    if (head == NULL)
    {
        return head;
    }
    struct ListNode *first = head, *second = head;

    for (int i = 0; i < k; i++)
    {
        first = first->next;
    }

    while(first != NULL)
    {
        first = first->next;
        second = second->next;
    }
    return second->val;
}