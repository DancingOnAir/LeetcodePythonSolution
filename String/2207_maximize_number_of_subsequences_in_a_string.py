class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        first, second = pattern
        first_num = second_num = 0
        res = 0
        for i in range(len(text) - 1, -1, -1):
            if text[i] == first:
                res += second_num
                first_num += 1
            elif text[i] == second:
                res += first_num
                second_num += 1

        return res + max(first_num, second_num)


def test_maximum_subsequence_count():
    solution = Solution()
    assert solution.maximumSubsequenceCount('abdcdbc', 'ac') == 4, 'wrong result'
    assert solution.maximumSubsequenceCount('aabb', 'ab') == 6, 'wrong result'


if __name__ == '__main__':
    test_maximum_subsequence_count()
