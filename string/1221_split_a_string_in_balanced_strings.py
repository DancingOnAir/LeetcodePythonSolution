from itertools import accumulate


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return list(accumulate(map({'L': 1, 'R': -1}.get, s))).count(0)

    def balancedStringSplit1(self, s: str) -> int:
        res = cnt = 0
        for c in s:
            cnt += 1 if c == 'L' else -1

            if not cnt:
                res += 1
        return res


def test_balanced_string_split():
    solution = Solution()

    assert solution.balancedStringSplit('RLRRLLRLRL') == 4, 'wrong result'
    assert solution.balancedStringSplit('RLLLLRRRLR') == 3, 'wrong result'
    assert solution.balancedStringSplit('LLLLRRRR') == 1, 'wrong result'
    assert solution.balancedStringSplit('RLRRRLLRLL') == 2, 'wrong result'


if __name__ == '__main__':
    test_balanced_string_split()
