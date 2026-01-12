class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        res = k % (2 * (n - 1))
        return res if res < n else 2 * (n - 1) - res


def test_number_of_child():
    solution = Solution()
    assert solution.numberOfChild(3, 5) == 1, 'wrong result'
    assert solution.numberOfChild(5, 6) == 2, 'wrong result'
    assert solution.numberOfChild(4, 2) == 2, 'wrong result'


if __name__ == '__main__':
    test_number_of_child()
