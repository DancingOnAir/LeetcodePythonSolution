from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        lo, hi = 1, n

        res = [0]
        for i, c in enumerate(s):
            if c == 'I':
                res.append(lo)
                lo += 1
            else:
                res.insert(i, hi)
                hi -= 1
        return res


def test_di_string_match():
    solution = Solution()

    assert solution.diStringMatch('IDID') == [0, 4, 1, 3, 2], 'wrong result'
    assert solution.diStringMatch('III') == [0, 1, 2, 3], 'wrong result'
    assert solution.diStringMatch('DDI') == [3, 2, 0, 1], 'wrong result'


if __name__ == '__main__':
    test_di_string_match()
