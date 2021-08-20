class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        if not word1 or not word2:
            return word1 + word2

        if word1 >= word2:
            return word1[0] + self.largestMerge(word1[1:], word2)

        return word2[0] + self.largestMerge(word1, word2[1:])




def test_largest_merge():
    solution = Solution()
    assert solution.largestMerge('cabaa', 'bcaaa') == 'cbcabaaaaa', 'wrong result'
    assert solution.largestMerge('abcabc', 'abdcaba') == 'abdcabcabcaba', 'wrong result'


if __name__ == '__main__':
    test_largest_merge()
