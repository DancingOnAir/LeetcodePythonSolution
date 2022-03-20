class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        pass


def test_is_additive_number():
    solution = Solution()
    assert solution.isAdditiveNumber('112358'), 'wrong result'
    assert solution.isAdditiveNumber('199100199'), 'wrong result'


if __name__ == '__main__':
    test_is_additive_number()
