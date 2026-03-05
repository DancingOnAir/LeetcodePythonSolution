from itertools import count


class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        x = 1 % k
        for i in count(1):
            if x == 0:
                return i
            x = (10 * x + 1) % k


def test_min_all_one_multiple():
    solution = Solution()
    assert solution.minAllOneMultiple(3) == 3, 'wrong result'
    assert solution.minAllOneMultiple(7) == 6, 'wrong result'
    assert solution.minAllOneMultiple(2) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_all_one_multiple()

