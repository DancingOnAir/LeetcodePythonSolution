from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def dfs(i):
            nonlocal cnt
            if all(x == 0 for x in m):
                nonlocal res
                res = max(res, cnt)

            if i == len(requests):
                return

            dfs(i + 1)

            m[requests[i][0]] -= 1
            m[requests[i][1]] += 1
            cnt += 1

            dfs(i + 1)

            m[requests[i][0]] += 1
            m[requests[i][1]] -= 1
            cnt -= 1

        res = cnt = 0
        m = [0] * n

        dfs(0)
        return res


def test_maximum_requests():
    solution = Solution()
    assert solution.maximumRequests(5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]) == 5, 'wrong result'
    assert solution.maximumRequests(3, [[0, 0], [1, 2], [2, 1]]) == 3, 'wrong result'


if __name__ == '__main__':
    test_maximum_requests()
