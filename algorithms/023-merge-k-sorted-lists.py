"""
合并K个排序链表

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_k_lists(lists: List[ListNode]) -> ListNode:
    def merge(l1: ListNode, l2: ListNode):
        if l1 is None or l2 is None:
            return l2 if l1 is None else l1
        else:
            dummy_head = curr = ListNode(None)
            p, q = l1, l2
            while p is not None and q is not None:
                if p.val < q.val:
                    curr.next = p
                    p = p.next
                else:
                    curr.next = q
                    q = q.next
                curr = curr.next

            if p is not None:
                curr.next = p
            elif q is not None:
                curr.next = q

            return dummy_head.next

    lists_len = len(lists)
    ans = None
    for i in range(lists_len):
        ans = merge(ans, lists[i])

    return ans



