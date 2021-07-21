from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for log in logs:
            if log == "../":
                res -= 1 if res > 0 else 0
            elif log == "./":
                continue
            else:
                res += 1

        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations(["d1/", "d2/", "../", "d21/", "./"]) == 2, 'wrong result'
    assert solution.minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]) == 3, 'wrong result'
    assert solution.minOperations(["d1/", "../", "../", "../"]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
