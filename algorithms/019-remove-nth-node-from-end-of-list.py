"""
删除链表的倒数第N个节点

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_list(nums):
    dummy_head = ListNode(None)
    p = dummy_head
    for num in nums:
        p.next = ListNode(num)
        p = p.next
    return dummy_head.next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy_head = ListNode(None)
    dummy_head.next = head
    p = q = dummy_head
    for i in range(n + 1):
        p = p.next

    while p is not None:
        p = p.next
        q = q.next

    q.next = q.next.next
    return dummy_head.next


if __name__ == '__main__':
    print(remove_nth_from_end(create_list([1, 2, 3, 4, 5]), 2))
    print(remove_nth_from_end(create_list([1]), 1))

