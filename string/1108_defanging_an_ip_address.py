class Solution:
    # split + join
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))

    def defangIPaddr2(self, address: str) -> str:
        res = ''
        for c in address:
            res += c if c.isdigit() else '[.]'

        return res

    # string replace
    def defangIPaddr1(self, address: str) -> str:
        return address.replace('.', '[.]')


def test_defang_ip_addr():
    solution = Solution()
    assert solution.defangIPaddr('1.1.1.1') == '1[.]1[.]1[.]1', 'wrong result'
    assert solution.defangIPaddr('255.100.50.0') == '255[.]100[.]50[.]0', 'wrong result'


if __name__ == '__main__':
    test_defang_ip_addr()
