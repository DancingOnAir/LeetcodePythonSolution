from typing import List
from collections import defaultdict


class Solution:
    # O(m) solution
    # https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/discuss/1647654/Python-Back-tracking-O(m)-Solution
    def executeInstructions(self, n, start, s):
        ns = len(s)
        (x0, y0), (x, y) = start, (0, 0)
        res = list(range(ns, 0, -1))
        count = defaultdict(set)
        count[x0, None].add(0)
        count[None, y0].add(0)

        for i in range(ns):
            if s[i] == 'L':
                y -= 1
            elif s[i] == 'R':
                y += 1
            elif s[i] == 'U':
                x -= 1
            elif s[i] == 'D':
                x += 1

            count[x0 - x, None].add(i + 1)
            count[None, y0 - y].add(i + 1)

            for key in [(n - x, None), (None, n - y), (-x - 1, None), (None, -y - 1)]:
                for j in count[key]:
                    if res[j] > i - j:
                        res[j] = i - j
                count[key] = set()
        return res

    # brute force
    def executeInstructions2(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)

        def mock(i):
            x, y = startPos
            for j in range(i, m):
                if s[j] == 'L':
                    y -= 1
                elif s[j] == 'R':
                    y += 1
                elif s[j] == 'U':
                    x -= 1
                else:
                    x += 1

                if not (0 <= x < n and 0 <= y < n):
                    return j - i
            return m - i

        return list(map(mock, range(m)))

    # initial version
    def executeInstructions1(self, n: int, startPos: List[int], s: str) -> List[int]:
        def get_num_instruction(s):
            # x, y
            moves = [0, 0]
            for i, ch in enumerate(s):
                if ch == 'R':
                    moves[0] += 1
                elif ch == 'L':
                    moves[0] -= 1
                elif ch == 'U':
                    moves[1] += 1
                else:
                    moves[1] -= 1

                if (moves[0] > 0 and moves[0] > limits[0]) or (moves[0] < 0 and abs(moves[0]) > limits[2]) or (
                        moves[1] > 0 and moves[1] > limits[3]) or (moves[1] < 0 and abs(moves[1]) > limits[1]):
                    return i

            return len(s)

        # RDLU
        limits = [n - 1 - startPos[1], n - 1 - startPos[0], startPos[1], startPos[0]]
        res = list()
        for i in range(len(s)):
            res.append(get_num_instruction(s[i:]))
        return res


def test_execute_instructions():
    solution = Solution()
    assert solution.executeInstructions(3, [0, 1], 'RRDDLU') == [1, 5, 4, 3, 1, 0], 'wrong result'
    assert solution.executeInstructions(2, [1, 1], 'LURD') == [4, 1, 0, 0], 'wrong result'
    assert solution.executeInstructions(1, [0, 0], 'LRUD') == [0, 0, 0, 0], 'wrong result'


if __name__ == '__main__':
    test_execute_instructions()
