class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        if k % 2 == 0:
            return 1 if self.kthGrammar(n - 1, k // 2) == 0 else 0
        return 1 if self.kthGrammar(n - 1, (k + 1) // 2) else 0


def test_kth_grammar():
    solution = Solution()
    assert solution.kthGrammar(1, 1) == 0, 'wrong result'
    assert solution.kthGrammar(2, 1) == 0, 'wrong result'
    assert solution.kthGrammar(2, 2) == 1, 'wrong result'


if __name__ == '__main__':
    test_kth_grammar()
