from typing import List
from collections import Counter


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        res = [0] * len(queries)
        seen = i = j = 0
        cnt = Counter()
        logs.sort(key=lambda l: l[1])
        for t, idx in sorted([t, idx] for idx, t in enumerate(queries)):
            while i < len(logs) and logs[i][1] <= t:
                cnt[logs[i][0]] += 1
                seen += cnt[logs[i][0]] == 1
                i += 1
            while j < i and logs[j][1] < t - x:
                cnt[logs[j][0]] -= 1
                seen -= cnt[logs[j][0]] == 0
                j += 1
            res[idx] = n - seen
        return res


def test_count_servers():
    solution = Solution()
    assert solution.countServers(3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11]) == [1, 2], 'wrong result'
    assert solution.countServers(3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4]) == [0, 1], 'wrong result'


if __name__ == '__main__':
    test_count_servers()
