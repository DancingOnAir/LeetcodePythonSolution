class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        zeros = binary.count('0')
        if zeros < 2:
            return binary
        first_zero = binary.find('0')
        return '1' * first_zero + '1' * (zeros - 1) + '0' + '1' * (len(binary) - first_zero - zeros)


def test_maximum_binary_string():
    solution = Solution()

    assert solution.maximumBinaryString("000110") == "111011", 'wrong result'
    assert solution.maximumBinaryString("01") == "01", 'wrong result'


if __name__ == '__main__':
    test_maximum_binary_string()
