class Solution:
    def maxProduct(self, s: str) -> int:
        pass


def test_max_product():
    solution = Solution()
    assert solution.maxProduct("leetcodecom") == 9, 'wrong result'
    assert solution.maxProduct("bb") == 1, 'wrong result'
    assert solution.maxProduct("accbcaxxcxx") == 25, 'wrong result'


if __name__ == '__main__':
    test_max_product()
