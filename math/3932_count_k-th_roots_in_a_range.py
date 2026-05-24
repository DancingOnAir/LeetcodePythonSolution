from math import ceil


class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        return int(round(r ** (1 / k), 10)) - ceil(l ** (1 / k)) + 1


def test_count_kth_roots():
    solution = Solution()
    assert solution.countKthRoots(1, r=9, k=3) == 2, 'wrong result'
    assert solution.countKthRoots(8, r=30, k=2) == 3, 'wrong result'


if __name__ == '__main__':
    test_count_kth_roots()
