class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add(ss):
            return ''.join(str((int(c) + a) % 10) if k & 1 else c for k, c in enumerate(ss))

        def rotate(ss):
            return ss[-b:] + ss[:-b]

        def dfs(ss):
            if ss not in seen:
                seen.add(ss)
                self.res = min(ss, self.res)

                dfs(add(ss))
                dfs(rotate(ss))

        self.res = s
        seen = set()
        dfs(s)
        return self.res


def test_find_lex_smallest_string():
    solution = Solution()
    # assert solution.findLexSmallestString('5525', 9, 2) == '2050', 'wrong result'
    assert solution.findLexSmallestString('74', 5, 1) == '24', 'wrong result'
    assert solution.findLexSmallestString('0011', 4, 2) == '0011', 'wrong result'
    assert solution.findLexSmallestString('43987654', 7, 3) == '00553311', 'wrong result'


if __name__ == '__main__':
    test_find_lex_smallest_string()
