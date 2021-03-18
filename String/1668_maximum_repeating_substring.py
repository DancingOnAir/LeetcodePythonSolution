class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        l1, l2 = len(sequence), len(word)
        if l1 < l2:
            return 0

        res = 0
        i = 1
        while l1 >= l2 * i:
            if word * i in sequence:
                res = i
            else:
                break
            i += 1
        return res


def test_max_repeating():
    solution = Solution()
    assert solution.maxRepeating('ababc', 'ab') == 2, 'wrong result'
    assert solution.maxRepeating('ababc', 'ba') == 1, 'wrong result'
    assert solution.maxRepeating('ababc', 'ac') == 0, 'wrong result'


if __name__ == '__main__':
    test_max_repeating()
