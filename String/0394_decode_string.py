class Solution:
    def decodeString(self, s: str) -> str:

        pass


def test_decode_string():
    solution = Solution()
    assert solution.decodeString("3[a]2[bc]") == "aaabcbc", 'wrong result'
    assert solution.decodeString("3[a2[c]]") == "accaccacc", 'wrong result'
    assert solution.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef", 'wrong result'


if __name__ == '__main__':
    test_decode_string()
