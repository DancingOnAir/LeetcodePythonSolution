class Solution:
    # TLE
    def largestMerge(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)

        if n1 == 0:
            return word2
        if n2 == 0:
            return word1
        if word1[0] > word2[0]:
            return word1[0] + self.largestMerge(word1[1:], word2)
        elif word1[0] < word2[0]:
            return word2[0] + self.largestMerge(word1, word2[1:])

        return max(word1[0] + self.largestMerge(word1[1:], word2), word2[0] + self.largestMerge(word1, word2[1:]))


def test_largest_merge():
    solution = Solution()
    assert solution.largestMerge('cabaa', 'bcaaa') == 'cbcabaaaaa', 'wrong result'
    assert solution.largestMerge('abcabc', 'abdcaba') == 'abdcabcabcaba', 'wrong result'


if __name__ == '__main__':
    test_largest_merge()
