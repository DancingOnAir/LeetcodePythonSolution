from typing import List
from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uams = defaultdict(set)
        for id, time in logs:
            uams[id].add(time)

        res = [0] * k
        for uam in uams.values():
            res[len(uam) - 1] += 1
        return res

    def findingUsersActiveMinutes1(self, logs: List[List[int]], k: int) -> List[int]:
        uam = defaultdict(set)
        for log in logs:
            uam[log[0]].add(log[1])

        m = defaultdict(int)
        for idx, times in uam.items():
            m[len(times)] += 1

        res = list()
        for i in range(1, k + 1):
            res.append(m[i])
        return res


def test_finding_users_active_minutes():
    solution = Solution()
    assert solution.findingUsersActiveMinutes([[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], 5) == [0, 2, 0, 0, 0], 'wrong result'
    assert solution.findingUsersActiveMinutes([[1, 1], [2, 2], [2, 3]], 4) == [1, 1, 0, 0], 'wrong result'


if __name__ == '__main__':
    test_finding_users_active_minutes()
