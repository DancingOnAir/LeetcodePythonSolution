from bisect import bisect_left


class Solution:
    # built-in binary search method in python 3.9
    def firstBadVersion(self, n: int) -> int:
        return bisect_left(range(n + 1), True, 1, key=isBadVersion)

    def firstBadVersion1(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 1


def test_first_bad_version():
    solution = Solution()
    # assert solution.firstBadVersion(5) == 4, 'wrong result'
    assert solution.firstBadVersion(1) == 1, 'wrong result'


if __name__ == '__main__':
    test_first_bad_version()
