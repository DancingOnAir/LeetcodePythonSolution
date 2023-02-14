from typing import List


class Solution:
    # https://leetcode.com/problems/h-index-ii/solutions/693380/python-2-solutions-binary-search-o-log-n-and-oneliner-o-n-explained/
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            # A scientist has an index h if h of their n papers have at least h citations each,
            # and the other n − h papers have no more than h citations each.
            if citations[mid] < n - mid:
                left = mid + 1
            elif citations[mid] > n - mid:
                right = mid - 1
            elif citations[mid] == n - mid:
                right = mid - 1

        return n - left


def test_h_index():
    solution = Solution()
    assert solution.hIndex([100, 100]) == 2, 'wrong result'
    assert solution.hIndex([100]) == 1, 'wrong result'
    assert solution.hIndex([0, 1, 3, 5, 6]) == 3, 'wrong result'
    assert solution.hIndex([1, 2, 100]) == 2, 'wrong result'


if __name__ == '__main__':
    test_h_index()
