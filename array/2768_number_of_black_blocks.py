from typing import List


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        res = [0] * 5
        s = set(map(tuple, coordinates))
        seen = set()
        for x, y in coordinates:
            for i in range(max(x - 1, 0), min(x + 1, m - 1)):
                for j in range(max(y - 1, 0), min(y + 1, n - 1)):
                    if (i, j) not in seen:
                        seen.add((i, j))
                        cnt = ((i, j) in s) + ((i, j + 1) in s) + ((i + 1, j) in s) + ((i + 1, j + 1) in s)
                        res[cnt] += 1
        res[0] = (m - 1) * (n - 1) - len(seen)
        return res

    # TLE
    def countBlackBlocks1(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        res = [0] * 5
        coordinates = set(tuple(x) for x in coordinates)
        for r in range(m - 1):
            for c in range(n - 1):
                cnt = 0
                if (r, c) in coordinates:
                    cnt += 1
                if r < m - 1 and (r + 1, c) in coordinates:
                    cnt += 1
                if c < n - 1 and (r, c + 1) in coordinates:
                    cnt += 1
                if r < m - 1 and c < n - 1 and (r + 1, c + 1) in coordinates:
                    cnt += 1
                res[cnt] += 1
        return res


def test_count_black_blocks():
    solution = Solution()
    assert solution.countBlackBlocks(3, 3, [[0, 0]]) == [3, 1, 0, 0, 0], 'wrong result'
    assert solution.countBlackBlocks(3, 3, [[0, 0], [1, 1], [0, 2]]) == [0, 2, 2, 0, 0], 'wrong result'


if __name__ == '__main__':
    test_count_black_blocks()
