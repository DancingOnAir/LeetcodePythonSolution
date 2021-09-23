from itertools import accumulate


class Solution:
    def maxProduct(self, s: str) -> int:
        def manachers(S):
            # 添加@作为起始标志，$作为结束标志
            A = "@#" + '#'.join(S) + "#$"
            R = [0] * len(A)
            # center表示目前最长回文字串的中心位置，right表示其最右边的位置
            center = right = 0

            for i in range(1, len(A) - 1):
                if right > i:
                    # 2 * center - i表示以center为中心，和i对称的在center的左边的位置j
                    R[i] = min(right - i, R[2 * center - i])
                while A[i + R[i] + 1] == A[i - R[i] - 1]:
                    R[i] += 1
                if i + R[i] > right:
                    center, right = i, i + R[i]
            # 跳过添加的字符，注意得到的结果是回文字长度，而不是一半，因为包含字符#的长度。
            return R[2: -2: 2]

        def helper(s):
            man, n = manachers(s), len(s)
            # 得到每个以位置i为中心，其最长回文字串的头尾位置
            ints = [(i - man[i] // 2, i + man[i] // 2) for i in range(n)]
            arr = [0] * n
            for a, b in ints:
                arr[b] = max(arr[b], b - a + 1)
            for i in range(n - 2, -1, -1):
                arr[i] = max(arr[i], arr[i + 1] - 2)
            return list(accumulate(arr, max))

        t1, t2 = helper(s), helper(s[::-1])[::-1][1:] + [0]
        return max(x * y for x, y in zip(t1, t2))


def test_max_product():
    solution = Solution()

    assert solution.maxProduct("ababbb") == 9, 'wrong result'
    assert solution.maxProduct("zaaaxbbby") == 9, 'wrong result'


if __name__ == '__main__':
    test_max_product()
