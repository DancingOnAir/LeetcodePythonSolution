class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))


def test_minimized_string_length():
    solution = Solution()
    assert solution.minimizedStringLength("aaabc") == 3, 'wrong result'
    assert solution.minimizedStringLength("cbbd") == 3, 'wrong result'
    assert solution.minimizedStringLength("dddaaa") == 2, 'wrong result'


if __name__ == '__main__':
    test_minimized_string_length()
