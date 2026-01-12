class Solution:
    # Prefix Sum and Suffix Sum
    # If we add p[0], the best option is to prepend it at the beginning.
    # If we add p[1], the best option is to append it at the end.
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        a = b = res = 0
        for c in text:
            if c == pattern[1]:
                res += a
            a += c == pattern[0]
            b += c == pattern[1]
        return res + max(a, b)

    # Use two if in solution,
    # to handle the corner case where pattern[0] == pattern[1].
    def maximumSubsequenceCount1(self, text: str, pattern: str) -> int:
        first, second = pattern
        first_num = second_num = 0
        res = 0
        for i in range(len(text) - 1, -1, -1):
            if text[i] == first:
                res += second_num
                first_num += 1
            if text[i] == second:
                second_num += 1

        return res + max(first_num, second_num)


def test_maximum_subsequence_count():
    solution = Solution()
    assert solution.maximumSubsequenceCount('abdcdbc', 'ac') == 4, 'wrong result'
    assert solution.maximumSubsequenceCount('aabb', 'ab') == 6, 'wrong result'


if __name__ == '__main__':
    test_maximum_subsequence_count()
