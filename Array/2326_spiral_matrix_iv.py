from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        pass


def test_spiral_matrix():
    solution = Solution()
    assert solution.spiralMatrix(3, 5, [3,0,2,6,8,1,7,9,4,2,5,5,0]) == [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]], 'wrong result'
    assert solution.spiralMatrix(1, 4, [0,1,2]) == [[0,1,2,-1]], 'wrong result'


if __name__ == '__main__':
    test_spiral_matrix()
