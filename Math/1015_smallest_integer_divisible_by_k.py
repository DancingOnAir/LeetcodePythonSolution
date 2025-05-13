from itertools import count


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        x = 1 % k
        for i in count(1):
            if x == 0:
                return i
            x = (x * 10 + 1) % k


def test_smallest_reunit_div_by_k():
    solution = Solution()
    assert solution.smallestRepunitDivByK(1) == 1, 'wrong result'
    assert solution.smallestRepunitDivByK(2) == -1, 'wrong result'
    assert solution.smallestRepunitDivByK(3) == 3, 'wrong result'


if __name__ == '__main__':
    test_smallest_reunit_div_by_k()
