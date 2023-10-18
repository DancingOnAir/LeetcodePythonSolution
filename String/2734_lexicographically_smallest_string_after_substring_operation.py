class Solution:
    def smallestString(self, s: str) -> str:
        def helper(x):
            return ''.join(map(lambda c: chr((ord(c) - 98) % 26 + 97), x))

        for i, c in enumerate(s):
            if c != 'a':
                cur = i
                nxt = s.find('a', cur + 1)
                return s[:cur] + helper(s[cur:nxt]) + s[nxt:] if nxt != -1 else s[:cur] + helper(s[cur:])
        return s[:-1] + 'z'


def test_smallest_string():
    solution = Solution()
    assert solution.smallestString("cbabc") == "baabc", 'wrong result'
    assert solution.smallestString("acbbc") == "abaab", 'wrong result'
    assert solution.smallestString("leetcode") == "kddsbncd", 'wrong result'


if __name__ == '__main__':
    test_smallest_string()
