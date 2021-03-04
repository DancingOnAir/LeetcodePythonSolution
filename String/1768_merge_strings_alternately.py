class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        min_l = min(l1, l2)
        res = [''] * (min_l * 2)

        for i in range(min_l):
            res[i * 2] = word1[i]
            res[i * 2 + 1] = word2[i]

        res = ''.join(res)
        if l1 > min_l:
            res += word1[min_l:]
        elif l2 > min_l:
            res += word2[min_l:]
        return res


def test_merge_alternately():
    solution = Solution()
    assert solution.mergeAlternately("abc", "pqr") == "apbqcr", 'wrong result'
    assert solution.mergeAlternately("ab", "pqrs") == "apbqrs", 'wrong result'
    assert solution.mergeAlternately("abcd", "pq") == "apbqcd", 'wrong result'


if __name__ == '__main__':
    test_merge_alternately()
