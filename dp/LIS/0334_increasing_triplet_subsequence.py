from bisect import bisect_left


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        g = []
        for x in nums:
            j = bisect_left(g, x)
            if j == 2:
                return True
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
        return False


def test_increasing_triplet():
    solution = Solution()
    assert solution.increasingTriplet([1, 2, 3, 4, 5]), 'wrong result'
    assert not solution.increasingTriplet([5, 4, 3, 2, 1]), 'wrong result'
    assert solution.increasingTriplet([2, 1, 5, 0, 4, 6]), 'wrong result'


if __name__ == '__main__':
    test_increasing_triplet()
