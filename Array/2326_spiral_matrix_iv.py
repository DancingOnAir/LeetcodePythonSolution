from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        r = c = 0
        dr, dc = 0, 1

        while head:
            res[r][c] = head.val
            if r + dr < 0 or r + dr >= m or c + dc < 0 or c + dc >= n or res[r + dr][c + dc] != -1:
                dr, dc = dc, -dr
            r += dr
            c += dc
            head = head.next

        return res


def test_spiral_matrix():
    solution = Solution()

    nums = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
    head = cur = ListNode(nums[0])
    for x in nums[1:]:
        cur.next = ListNode(x)
        cur = cur.next
    assert solution.spiralMatrix(3, 5, head) == [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]], 'wrong result'

    nums = [0, 1, 2]
    head = cur = ListNode(nums[0])
    for x in nums[1:]:
        cur.next = ListNode(x)
        cur = cur.next
    assert solution.spiralMatrix(1, 4, head) == [[0, 1, 2, -1]], 'wrong result'


if __name__ == '__main__':
    test_spiral_matrix()
