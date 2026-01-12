class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def helper(i, j, k):
            if i <= k <= j:
                return 0
            if k < i:
                return i - k
            return k - j

        x = helper(x1, x2, xCenter)
        y = helper(y1, y2, yCenter)
        return x * x + y * y <= radius * radius


def test_check_overlap():
    solution = Solution()
    assert solution.checkOverlap(1, xCenter=0, yCenter=0, x1=1, y1=-1, x2=3, y2=1), 'wrong result'
    assert not solution.checkOverlap(1, xCenter=1, yCenter=1, x1=1, y1=-3, x2=2, y2=-1), 'wrong result'
    assert solution.checkOverlap(1, xCenter=0, yCenter=0, x1=-1, y1=0, x2=0, y2=1), 'wrong result'


if __name__ == '__main__':
    test_check_overlap()
