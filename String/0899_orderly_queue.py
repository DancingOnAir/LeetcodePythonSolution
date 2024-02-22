class Solution:
    # k > 1 任何字母都能互换，s可以表示成任意的组合
    # k == 1, 就是循环数组
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        return min(s[i:] + s[:i] for i in range(len(s)))


def test_orderly_queue():
    solution = Solution()
    assert solution.orderlyQueue("cba", 1) == "acb", 'wrong result'
    assert solution.orderlyQueue("baaca", 3) == "aaabc", 'wrong result'


if __name__ == '__main__':
    test_orderly_queue()
