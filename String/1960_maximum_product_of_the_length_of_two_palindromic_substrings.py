class Solution:
    def maxProduct(self, s: str) -> int:
        pass


def test_max_product():
    solution = Solution()

    assert solution.maxProduct("ababbb") == 9, 'wrong result'
    assert solution.maxProduct("zaaaxbbby") == 9, 'wrong result'


if __name__ == '__main__':
    test_max_product()
