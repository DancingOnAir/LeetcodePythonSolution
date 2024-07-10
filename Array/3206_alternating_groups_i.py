from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors += colors[:2]
        res = 0
        for i in range(len(colors) - 2):
            if colors[i] ^ colors[i + 1] and colors[i + 1] ^ colors[i + 2]:
                res += 1
        return res


def test_number_of_alternating_groups():
    solution = Solution()
    assert solution.numberOfAlternatingGroups([1, 1, 1]) == 0, 'wrong result'
    assert solution.numberOfAlternatingGroups([0, 1, 0, 0, 1]) == 3, 'wrong result'


if __name__ == '__main__':
    test_number_of_alternating_groups()
