class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        res = i = j = 0
        while i < len(s):
            while j < len(s) and int(s[i: j + 1]) <= k:
                j += 1

            if i == j:
                return -1
            res += 1
            i = j
        return res


def test_minimum_partition():
    solution = Solution()
    assert solution.minimumPartition("165462", 60) == 4, 'wrong result'
    assert solution.minimumPartition("238182", 5) == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_partition()
