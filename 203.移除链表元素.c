/*
 * @lc app=leetcode.cn id=203 lang=c
 *
 * [203] 移除链表元素
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdlib.h>
#include <stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode *p_head, *before;

    if (head == NULL)
        return head;

    while (head != NULL)
    {
        // 先移动到不是val的点
        if (head->val == val)
        {
            head = head->next;
        }
        else
        {
            break;
        }
    }

    p_head = head;
    while (p_head != NULL)
    {
        if (p_head->val == val)
        {
            // 如果当前节点是val,则不断向后移动
            while(p_head->val == val)
            {
                if (p_head->next == NULL)
                {
                    // 移动到最后
                   p_head = NULL;
                   break;
                }
                p_head = p_head->next;
            }
            // 去掉等于val的点
            before->next = p_head;
        }
        before = p_head;
        if (p_head != NULL)
            p_head = p_head->next;
    }
    return head;
}
// @lc code=end

