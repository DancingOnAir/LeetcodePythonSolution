from typing import List
from collections import deque


class Solution:
    # bfs
    def openLock(self, deadends: List[str], target: str) -> int:
        m = set(deadends)
        if '0000' in m:
            return -1

        dq = deque([(0, '0000')])
        while dq:
            step, code = dq.popleft()
            if code == target:
                return step

            for i in range(4):
                d = int(code[i])
                for k in (d - 1) % 10, (d + 1) % 10:
                    cand = code[:i] + str(k) + code[i+1:]
                    if cand not in m:
                        m.add(cand)
                        dq.append((step + 1, cand))
        return -1


def test_open_lock():
    solution = Solution()
    assert solution.openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6, 'wrong result'
    assert solution.openLock(["8888"], "0009") == 1, 'wrong result'
    assert solution.openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
                             "8888") == -1, 'wrong result'


if __name__ == '__main__':
    test_open_lock()
