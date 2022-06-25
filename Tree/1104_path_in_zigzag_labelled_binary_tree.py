from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        pass


def test_path_in_zigzag_tree():
    solution = Solution()
    assert solution.pathInZigZagTree(14) == [1, 3, 4, 14], 'wrong result'
    assert solution.pathInZigZagTree(26) == [1, 2, 6, 10, 26], 'wrong result'


if __name__ == '__main__':
    test_path_in_zigzag_tree()
