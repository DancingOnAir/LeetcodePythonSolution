from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        s += fill * ((k - n % k) % k)
        return [s[i*k: (i+1)*k] for i in range(len(s) // k)]


def test_divide_string():
    solution = Solution()
    assert solution.divideString("abcdefghi", 3, "x") == ["abc", "def", "ghi"], 'wrong result'
    assert solution.divideString("abcdefghij", 3, "x") == ["abc", "def", "ghi", "jxx"], 'wrong result'


if __name__ == '__main__':
    test_divide_string()
