class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left_zeros = [-1]
        cnt1 = res = 0

        for r, c in enumerate(s):
            if c == '0':
                left_zeros.append(r)
            else:
                # 不含0子串的个数，以r为子串的右端点
                res += r - left_zeros[-1]
                cnt1 += 1
            for k in range(len(left_zeros) - 1, 0, -1):
                zeros = len(left_zeros) - k
                if zeros * zeros > cnt1:
                    break
                ones = r - left_zeros[k] + 1 - zeros
                d = max(0, zeros * zeros - ones)
                res += max(0, left_zeros[k] - left_zeros[k - 1] - d)
        return res


def test_number_of_substrings():
    solution = Solution()
    assert solution.numberOfSubstrings("00011") == 5, 'wrong result'
    assert solution.numberOfSubstrings("101101") == 16, 'wrong result'


if __name__ == '__main__':
    test_number_of_substrings()
