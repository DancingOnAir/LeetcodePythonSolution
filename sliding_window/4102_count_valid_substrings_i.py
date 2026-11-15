class Solution:
    def countValidSubstrings(self, s: str) -> int:
        res = -s.count("abc")
        # count 'b' twice
        for p in s.replace("abc", "ab bc").split():
            res += len(p) * (len(p) + 1) // 2
        return res


def test_count_valid_substrings():
    solution = Solution()
    assert solution.countValidSubstrings("abac") == 10, 'wrong result'
    assert solution.countValidSubstrings("abc") == 5, 'wrong result'
    assert solution.countValidSubstrings("ac") == 3, 'wrong result'


if __name__ == "__main__":
    test_count_valid_substrings()
