class Solution:
    # pythonic greedy
    def minimumPartition(self, s: str, k: int) -> int:
        # 这里res初始化为1，是因为最后一个满足要求的字符串总是没有被统计，比如s='62', k=7
        res, cur = 1, 0
        for v in map(int, s):
            if v > k:
                return -1

            cur = cur * 10 + v
            if cur > k:
                res += 1
                cur = v
        return res

    # greedy
    def minimumPartition1(self, s: str, k: int) -> int:
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
