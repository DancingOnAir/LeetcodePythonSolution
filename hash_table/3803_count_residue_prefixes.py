class Solution:
    def residuePrefixes(self, s: str) -> int:
        cnt = set()
        res = 0
        for i, c in enumerate(s):
            cnt.add(c)
            if len(cnt) == (i + 1) % 3:
                res += 1
        return res


def test_residue_prefixes():
    solution = Solution()
    assert solution.residuePrefixes("abc") == 2, 'wrong result'
    assert solution.residuePrefixes("dd") == 1, 'wrong result'
    assert solution.residuePrefixes("bob") == 2, 'wrong result'


if __name__ == '__main__':
    test_residue_prefixes()
