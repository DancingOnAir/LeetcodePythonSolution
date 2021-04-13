from itertools import groupby


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        memo = sorted([len(list(g)) for _, g in groupby(s)])
        print(memo)

        res = 0
        for i in memo:
            if k > 0:
                if k >= i:
                    k -= i
                    continue
                else:
                    i -= k
                    k = 0

            if i < 2:
                res += 1
            elif i < 9:
                res += 2
            else:
                res += 3

        return res


def test_get_length_of_optimal_compression():
    solution = Solution()
    assert solution.getLengthOfOptimalCompression('aaabcccd', 2) == 4, 'wrong result'
    assert solution.getLengthOfOptimalCompression('aabbaa', 2) == 2, 'wrong result'
    assert solution.getLengthOfOptimalCompression('aaaaaaaaaaa', 0) == 3, 'wrong result'


if __name__ == '__main__':
    test_get_length_of_optimal_compression()
