class Solution:
    def kthDigit(self, k: int) -> int:
        k -= 1
        cnt, length = 9, 1
        while cnt * length <= k:
            k -= cnt * length
            cnt *= 10
            length += 1
        # 确定是哪个数
        x = cnt // 9 + k // length
        # 确定上一轮的b奇偶性， 如果是奇数，那么需要逆序
        if x // 10 % 2 == 1:
            x += 9 - (x % 10) * 2
        tail = 10 ** (length - k % length - 1)
        return x // tail % 10


def test_kth_digit():
    solution = Solution()
    assert solution.kthDigit(4) == 4, 'wrong result'
    assert solution.kthDigit(15) == 7, 'wrong result'
    assert solution.kthDigit(11) == 9, 'wrong result'


if __name__ == '__main__':
    test_kth_digit()
