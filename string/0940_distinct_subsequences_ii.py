class Solution:
    # https://leetcode.com/problems/distinct-subsequences-ii/discuss/192017/C%2B%2BJavaPython-4-lines-O(N)-Time-O(1)-Space
    def distinctSubseqII(self, s: str) -> int:
        endWith = [0] * 26
        for c in s:
            endWith[ord(c) - ord('a')] = sum(endWith) + 1
        return sum(endWith) % (10 ** 9 + 7)


def test_distinct_subseq_ii():
    solution = Solution()

    assert solution.distinctSubseqII("abc") == 7, 'wrong result'
    assert solution.distinctSubseqII("aba") == 6, 'wrong result'
    assert solution.distinctSubseqII("abc") == 7, 'wrong result'


if __name__ == '__main__':
    test_distinct_subseq_ii()
