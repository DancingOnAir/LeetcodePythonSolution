class Solution:
    def minInteger(self, num: str, k: int) -> str:
        if k <= 0:
            return num

        n = len(num)
        if k >= n * (n - 1) // 2:
            return ''.join(sorted(num))

        for i in range(10):
            idx = num.find(str(i))
            if 0 <= idx <= k:
                return num[idx] + self.minInteger(num[:idx] + num[idx+1:], k - idx)

    # brute force
    def minInteger1(self, num: str, k: int) -> str:
        sorted_num = ''.join(sorted(num))
        start = 0
        while k > 0:
            if sorted_num == num:
                return num

            end = min(k + 1, len(num[start:])) + start
            min_num = min(num[start: end])
            min_pos = num.find(min_num, start, end)

            num = num[: start] + num[min_pos] + num[start: min_pos] + num[min_pos + 1:]
            k -= (min_pos - start)
            start += 1
        return num


def test_min_integer():
    solution = Solution()

    assert solution.minInteger("4321", 4) == "1342", 'wrong result'
    assert solution.minInteger("100", 1) == "010", 'wrong result'
    assert solution.minInteger("36789", 1000) == "36789", 'wrong result'
    assert solution.minInteger("22", 22) == "22", 'wrong result'
    assert solution.minInteger("9438957234785635408", 23) == "0345989723478563548", 'wrong result'


if __name__ == '__main__':
    test_min_integer()
