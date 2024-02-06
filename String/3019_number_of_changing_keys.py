from itertools import groupby


class Solution:
    def countKeyChanges(self, s: str) -> int:
        return len(list(groupby(s.lower()))) - 1

    def countKeyChanges1(self, s: str) -> int:
        res = 0
        pre = s[0].lower()
        for i in range(1, len(s)):
            if pre != s[i].lower():
                res += 1
            pre = s[i].lower()
        return res


def test_count_key_changes():
    solution = Solution()
    assert solution.countKeyChanges("aAbBcC") == 2, 'wrong result'
    assert solution.countKeyChanges("AaAaAaaA") == 0, 'wrong result'


if __name__ == '__main__':
    test_count_key_changes()
