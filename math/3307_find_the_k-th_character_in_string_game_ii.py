from typing import List
from string import ascii_lowercase


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        if not operations:
            return 'a'
        op = operations.pop()
        m = 1 << len(operations)
        if k <= m:
            return self.kthCharacter(k, operations)
        res = self.kthCharacter(k - m, operations)
        return ascii_lowercase[(ord(res) - ord('a') + op) % 26]


def test_kth_character():
    solution = Solution()
    assert solution.kthCharacter(5, [0, 0, 0]) == 'a', 'wrong result'
    assert solution.kthCharacter(10, [0, 1, 0, 1]) == 'b', 'wrong result'


if __name__ == '__main__':
    test_kth_character()
