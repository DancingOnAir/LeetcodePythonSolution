from typing import List


class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        res = []
        cur = ""
        for c in s:
            cur += c
            if cur not in seen:
                seen.add(cur)
                res.append(cur)
                cur = ""

        return res


def test_partition_string():
    solution = Solution()
    assert solution.partitionString("abbccccd") == ["a","b","bc","c","cc","d"], 'wrong result'
    assert solution.partitionString("aaaa") == ["a", "aa"], 'wrong result'


if __name__ == '__main__':
    test_partition_string()
