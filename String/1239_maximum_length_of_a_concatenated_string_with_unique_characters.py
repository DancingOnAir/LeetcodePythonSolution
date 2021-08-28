from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]

        for a in arr:
            if len(set(a)) < len(a):
                continue
            a = set(a)
            for d in dp[:]:
                if a & d:
                    continue
                dp.append(a | d)
        return max(len(d) for d in dp)


def test_max_length():
    solution = Solution()

    assert solution.maxLength(["un", "iq", "ue"]) == 4, 'wrong result'
    assert solution.maxLength(["cha", "r", "act", "ers"]) == 6, 'wrong result'
    assert solution.maxLength(["abcdefghijklmnopqrstuvwxyz"]) == 26, 'wrong result'


if __name__ == '__main__':
    test_max_length()

