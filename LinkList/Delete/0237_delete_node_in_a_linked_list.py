class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


def test_delete_node():
    def print_linked_list(head):
        res = list()
        while head:
            res.append(head.val)
            head = head.next
        return res

    solution = Solution()
    head = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
    solution.deleteNode(head.next)
    assert print_linked_list(head) == [4, 1, 9], 'wrong result'


if __name__ == '__main__':
    test_delete_node()
