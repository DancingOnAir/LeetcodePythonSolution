from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return []

        res = list()
        path = list()

        def dfs(i):
            if i == n:
                res.append(path.copy())
                return

            dfs(i + 1)
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

        dfs(0)
        return res


def test_subsets():
    solution = Solution()
    assert sorted(solution.subsets([1, 2, 3])) == sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]), 'wrong result'
    assert solution.subsets([0]) == [[], [0]], 'wrong result'


if __name__ == '__main__':
    test_subsets()
    # 测试深浅拷贝
    import copy

    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [a, b]

    d = c  # 直接赋值，浅拷贝
    print("c的内存地址为：%s" % id(c))
    print("d的内存地址为：%s" % id(d))

    # 使用copy模块
    # 深拷贝，重新开辟内存，并内容独立
    e = copy.deepcopy(c)
    # 深拷贝，重新开辟内存，但是新内容里面仍保存原来的引用
    f = copy.copy(c)
    # 打印e，f的地址
    print("e的内存地址为：%s" % id(e))
    print("f的内存地址为：%s" % id(f))

    # 改变a的值
    a.append(44)

    # 打印a,b,c,d,e,f
    print("a = %s" % a)
    print("b = %s" % b)
    print("c = %s" % c)
    print("d = %s" % d)
    print("e = %s" % e)
    print("f = %s" % f)
