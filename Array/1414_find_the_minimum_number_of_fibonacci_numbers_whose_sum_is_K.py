from typing import List


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def get_next_fibonacci_number(num):
            fibonacci_num = 0
            count = 0
            a, b = 1, 1
            while num > fibonacci_num:
                count += 1
                if count == 1:
                    fibonacci_num = a
                elif count == 2:
                    fibonacci_num = b
                else:
                    fibonacci_num = a + b
                    a = b
                    b = fibonacci_num
            return b if fibonacci_num == num else a

        res = 0
        target = k
        while target:
            target -= get_next_fibonacci_number(target)
            res += 1

        return res


def test_find_min_fibonacci_numbers():
    solution = Solution()

    print(solution.findMinFibonacciNumbers(7))
    print(solution.findMinFibonacciNumbers(10))
    print(solution.findMinFibonacciNumbers(19))


if __name__ == '__main__':
    test_find_min_fibonacci_numbers()
