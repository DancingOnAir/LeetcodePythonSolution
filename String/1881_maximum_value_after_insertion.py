class Solution:
    def maxValue(self, n: str, x: int) -> str:
        n = list(n)
        x = str(x)
        if n[0] == '-':
            for i in range(1, len(n)):
                if n[i] > x:
                    n.insert(i, x)
                    break

                if i == len(n) - 1:
                    n.append(x)
        else:
            for i in range(len(n)):
                if n[i] < x:
                    n.insert(i, x)
                    break
                if i == len(n) - 1:
                    n.append(x)
        return ''.join(n)


def test_max_value():
    solution = Solution()
    assert solution.maxValue("-132", 3) == "-1323", 'wrong result'
    assert solution.maxValue("99", 9) == "999", 'wrong result'
    assert solution.maxValue("-13", 2) == "-123", 'wrong result'


if __name__ == '__main__':
    test_max_value()
