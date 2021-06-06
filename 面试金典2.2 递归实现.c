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
// 递归实现。

int link_size = 0;
int kthToLast(struct ListNode *head, int k)
{
    int val;
    if (head == NULL)
    {
        link_size = 0; // 防止多次调用时 大小错误。
        return 0;
    }

    val = kthToLast(head->next, k);
    if (++link_size == k)
        return head->val;

    return val;
}