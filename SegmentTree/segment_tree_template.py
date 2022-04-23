from typing import List


# 比较传统的模式，使用list来存储每个节点的值，比如求和/最大值/最小值
class SegmentTree:
    def __init__(self, data, merge):
        '''
        data:传入的数组
        merge:处理的业务逻辑，例如求和/最大值/最小值，lambda表达式
        '''

        self.data = data
        self.n = len(data)
        #  申请4倍data长度的空间来存线段树节点
        self.tree = [None] * (4 * self.n) # 索引i的左孩子索引为2i+1，右孩子为2i+2
        self._merge = merge
        if self.n:
            self._build(0, 0, self.n-1)

    def query(self, ql, qr):
        '''
        返回区间[ql,..,qr]的值
        '''
        return self._query(0, 0, self.n-1, ql, qr)

    def update(self, index, value):
        # 将data数组index位置的值更新为value,然后递归更新线段树中被影响的各节点的值
        self.data[index] = value
        self._update(0, 0, self.n-1, index)

    def _build(self, tree_index, l, r):
        '''
        递归创建线段树
        tree_index : 线段树节点在数组中位置
        l, r : 该节点表示的区间的左,右边界
        '''
        if l == r:
            self.tree[tree_index] = self.data[l]
            return
        mid = (l+r) // 2 # 区间中点,对应左孩子区间结束,右孩子区间开头
        left, right = 2 * tree_index + 1, 2 * tree_index + 2 # tree_index的左右子树索引
        self._build(left, l, mid)
        self._build(right, mid+1, r)
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])

    def _query(self, tree_index, l, r, ql, qr):
        '''
        递归查询区间[ql,..,qr]的值
        tree_index : 某个根节点的索引
        l, r : 该节点表示的区间的左右边界
        ql, qr: 待查询区间的左右边界
        '''
        if l == ql and r == qr:
            return self.tree[tree_index]

        mid = (l+r) // 2 # 区间中点,对应左孩子区间结束,右孩子区间开头
        left, right = tree_index * 2 + 1, tree_index * 2 + 2
        if qr <= mid:
            # 查询区间全在左子树
            return self._query(left, l, mid, ql, qr)
        elif ql > mid:
            # 查询区间全在右子树
            return self._query(right, mid+1, r, ql, qr)

        # 查询区间一部分在左子树一部分在右子树
        return self._merge(self._query(left, l, mid, ql, mid),
                          self._query(right, mid+1, r, mid+1, qr))

    def _update(self, tree_index, l, r, index):
        '''
        tree_index:某个根节点索引
        l, r : 此根节点代表区间的左右边界
        index : 更新的值的索引
        '''
        if l == r == index:
            self.tree[tree_index] = self.data[index]
            return
        mid = (l+r)//2
        left, right = 2 * tree_index + 1, 2 * tree_index + 2
        if index > mid:
            # 要更新的区间在右子树
            self._update(right, mid+1, r, index)
        else:
            # 要更新的区间在左子树index<=mid
            self._update(left, l, mid, index)
        # 里面的小区间变化了，包裹的大区间也要更新
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])


# 给你一个数组 nums ，请你完成两类查询，其中一类查询要求更新数组下标对应的值，另一类查询要求返回数组中某个范围内元素的总和。
# 实现 NumArray 类：
# NumArray(int[] nums) 用整数数组 nums 初始化对象
# void update(int index, int val) 将 nums[index] 的值更新为 val
# int sumRange(int left, int right) 返回子数组 nums[left, right] 的总和（即，nums[left] + nums[left + 1], ..., nums[right]）
class NumArray:
    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(nums, lambda x, y: x + y)

    def update(self, i: int, val: int) -> None:
        self.segment_tree.update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.segment_tree.query(i, j)





# 线段树的节点类
class TreeNode(object):
    def __init__(self):
        self.left = -1
        self.right = -1
        self.sum_num = 0

    # 打印函数
    def __str__(self):
        return '[%s,%s,%s]' % (self.left, self.right, self.sum_num)

    # 打印函数
    def __repr__(self):
        return '[%s,%s,%s]' % (self.left, self.right, self.sum_num)


# 线段树类
# 以_开头的是递归实现
class Tree(object):
    def __init__(self, n, arr):
        self.n = n
        self.max_size = 4 * n
        self.tree = [TreeNode() for i in range(self.max_size)]  # 维护一个TreeNode数组
        self.arr = arr

    # index从1开始
    def _build(self, index, left, right):
        self.tree[index].left = left
        self.tree[index].right = right
        if left == right:
            self.tree[index].sum_num = self.arr[left - 1]
        else:
            mid = (left + right) // 2
            self._build(index * 2, left, mid)
            self._build(index * 2 + 1, mid + 1, right)
            self.pushup_sum(index)

    # 构建线段树
    def build(self):
        self._build(1, 1, self.n)

    def _update(self, point, val, i, l, r, ):
        if self.tree[i].left == self.tree[i].right:
            self.tree[i].sum_num += val
        else:
            mid = (l + r) // 2
            if point <= mid:
                self._update(point, val, i * 2, l, mid)
            else:
                self._update(point, val, i * 2 + 1, mid + 1, r)
                # 根据左右子树更新当前的值
            self.pushup_sum(i)

    # 单点更新
    # point 要更新的数在数组的下标 val更新的值
    def update(self, point, val, ):
        self._update(point, val, 1, 1, self.n)

    # 求和
    def pushup_sum(self, k):
        self.tree[k].sum_num = self.tree[k * 2].sum_num + self.tree[k * 2 + 1].sum_num

    def _query(self, ql, qr, i, l, r, ):
        if l >= ql and r <= qr:  # 若当前范围包含于要查询的范围
            return self.tree[i].sum_num
        else:
            mid = (l + r) // 2
            res_l = 0
            res_r = 0
            if ql <= mid:  # 左子树最大的值大于了查询范围最小的值-->左子树和需要查询的区间交集非空
                res_l = self._query(ql, qr, i * 2, l, mid, )
            if qr > mid:  # 右子树最小的值小于了查询范围最大的值-->右子树和需要查询的区间交集非空
                res_r = self._query(ql, qr, i * 2 + 1, mid + 1, r, )
            return res_l + res_r

    # 区间查询
    def query(self, ql, qr):
        return self._query(ql, qr, 1, 1, self.n)

    # 深度遍历打印数组
    def _show_arr(self, i):
        if self.tree[i].left == self.tree[i].right and self.tree[i].left != -1:
            print(self.tree[i].sum_num, end=" ")
        if 2 * i < len(self.tree):
            self._show_arr(i * 2)
            self._show_arr(i * 2 + 1)

    # 显示更新后的数组的样子
    def show_arr(self, ):
        self._show_arr(1)


# 测试用例1
def test():
    n = 5  # 1 5 4 2 3
    arr = [1, 5, 4, 2, 3]
    tree = Tree(n, arr)
    tree.build()
    tree.update(1, 3)
    res = tree.query(2, 5)
    print(res)
    tree.update(3, -1)
    tree.update(4, 2)
    res = tree.query(1, 4)
    print(res)


