from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        freq = Counter(s)
        for ch in order:
            if ch in freq:
                res.append(ch * freq[ch])

        for ch in s:
            if ch not in order:
                res.append(ch)
        return ''.join(res)


def test_custom_sort_string():
    solution = Solution()
    assert solution.customSortString("cba", "abcd") == "cbad", 'wrong result'
    assert solution.customSortString("cbafg", "abcd") == "cbad", 'wrong result'


if __name__ == '__main__':
    test_custom_sort_string()
