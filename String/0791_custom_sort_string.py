from collections import Counter


class Solution:
    # sort
    def customSortString(self, order: str, s: str) -> str:
        c = Counter()
        for i, ch in enumerate(order):
            c[ch] = i + 1

        return ''.join(sorted(s, key=lambda x: c[x]))

    # Counter method
    def customSortString1(self, order: str, s: str) -> str:
        res = []
        freq = Counter(s)
        for ch in order:
            if ch in freq:
                res.append(ch * freq[ch])
                freq[ch] = 0

        for ch in s:
            # if ch not in order:
            if freq[ch] > 0:
                res.append(ch)
        return ''.join(res)


def test_custom_sort_string():
    solution = Solution()
    assert solution.customSortString("cba", "abcd") == "cbad", 'wrong result'
    assert solution.customSortString("cbafg", "abcd") == "cbad", 'wrong result'


if __name__ == '__main__':
    test_custom_sort_string()
