class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def helper(x, y):
            n = int(x ** 0.5)
            m = int(((4 * y + 1) ** 0.5 - 1) / 2)
            if n > m:
                return 2 * m + 1
            return 2 * n

        return max(helper(red, blue), helper(blue, red))


def test_max_height_of_triangle():
    solution = Solution()
    assert solution.maxHeightOfTriangle(9, 3) == 3, 'wrong result'
    assert solution.maxHeightOfTriangle(2, 4) == 3, 'wrong result'
    assert solution.maxHeightOfTriangle(2, 1) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_height_of_triangle()
