from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return list(map(int, sorted(str(i) for i in range(1, n + 1))))


def test_lexical_order():
    solution = Solution()
    assert solution.lexicalOrder(13) == [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], 'wrong result'
    assert solution.lexicalOrder(2) == [1, 2], 'wrong result'


if __name__ == '__main__':
    test_lexical_order()
