class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


def test_min_partitions():
    solution = Solution()

    assert solution.minPartitions("32") == 3
    assert solution.minPartitions("82734") == 8
    assert solution.minPartitions("27346209830709182346") == 9


if __name__ == '__main__':
    test_min_partitions()
