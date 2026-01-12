from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        res = cnt = 0
        for i in range(n + k - 1):
            if colors[i % n] ^ colors[(i + 1) % n] == 0:
                cnt = 0
            cnt += 1
            if cnt >= k:
                res += 1
        return res

    # TLE
    def numberOfAlternatingGroups1(self, colors: List[int], k: int) -> int:
        n = len(colors)
        colors += colors[:k - 1]
        res = i = 0
        while i < n:
            alternated = True
            j = i
            while j < i + k - 1:
                if colors[j] ^ colors[j + 1] == 0:
                    alternated = False
                    break
                j += 1

            if alternated:
                i += 1
                res += 1
            else:
                i = j + 1
        return res


def test_number_of_alternating_groups():
    solution = Solution()
    assert solution.numberOfAlternatingGroups([0, 1, 0, 1, 1], 4) == 2, 'wrong result'
    assert solution.numberOfAlternatingGroups([0, 1, 0, 1, 0], 3) == 3, 'wrong result'
    assert solution.numberOfAlternatingGroups([0, 1, 0, 0, 1, 0, 1], 6) == 2, 'wrong result'
    assert solution.numberOfAlternatingGroups([1, 1, 0, 1], 4) == 0, 'wrong result'


if __name__ == '__main__':
    test_number_of_alternating_groups()
