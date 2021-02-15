"""
两数相加

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
#     p, q = l1, l2
#     curr = head = ListNode(None)
#     carry = 0
#     while p is not None and q is not None:
#         val = p.val + q.val + carry
#         if val >= 10:
#             val = val % 10
#             carry = 1
#         else:
#             carry = 0
#
#         curr.next = ListNode(val)
#         curr = curr.next
#         p, q = p.next, q.next
#
#     if carry == 0:
#         if p is not None:
#             curr.next = p
#         elif q is not None:
#             curr.next = q
#     else:
#         while p is not None:
#             val = p.val + carry
#             if val >= 10:
#                 val = val % 10
#                 curr.next = ListNode(val)
#                 curr = curr.next
#             else:
#                 curr.next = ListNode(val)
#                 curr = curr.next
#                 curr.next = p.next
#                 carry = 0
#                 break
#             p = p.next
#
#         while q is not None:
#             val = q.val + carry
#             if val >= 10:
#                 val = val % 10
#                 curr.next = ListNode(val)
#                 curr = curr.next
#             else:
#                 curr.next = ListNode(val)
#                 curr = curr.next
#                 curr.next = q.next
#                 carry = 0
#                 break
#             q = q.next
#
#         if carry == 1:
#             curr.next = ListNode(1)
#
#     return head.next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    p, q = l1, l2
    curr = head = ListNode(None)
    carry = 0
    while p is not None or q is not None:
        pval = p.val if p is not None else 0
        qval = q.val if q is not None else 0
        val = pval + qval + carry
        if val >= 10:
            val = val % 10
            carry = 1
        else:
            carry = 0

        curr.next = ListNode(val)
        curr = curr.next
        if p is not None:
            p = p.next
        if q is not None:
            q = q.next

    if carry == 1:
        curr.next = ListNode(1)

    return head.next


if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(8)
    l2 = ListNode(1)
    print(add_two_numbers(l1, l2))

