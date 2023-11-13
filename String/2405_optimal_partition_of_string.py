class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        m = set()
        for ch in s:
            if ch in m:
                res += 1
                m.clear()
            m.add(ch)
        return res + 1


def test_partition_string():
    solution = Solution()
    assert solution.partitionString("abacaba") == 4, 'wrong result'
    assert solution.partitionString("ssssss") == 6, 'wrong result'


if __name__ == '__main__':
    test_partition_string()
