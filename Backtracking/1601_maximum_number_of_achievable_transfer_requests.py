from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        pass


def test_maximum_requests():
    solution = Solution()
    assert solution.maximumRequests(5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]) == 5, 'wrong result'
    assert solution.maximumRequests(3, [[0, 0], [1, 2], [2, 1]]) == 3, 'wrong result'


if __name__ == '__main__':
    test_maximum_requests()
