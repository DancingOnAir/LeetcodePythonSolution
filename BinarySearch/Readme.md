##Reference
https://medium.com/@hazemu/useful-insights-into-binary-search-problems-8769d388b9c
https://leetcode-cn.com/circle/article/bNaUjl/

#Binary Search Template
二分查找主要分为两种形式：
- 基础形式
- 变体

下面所有介绍都是默认数组递增排序的。

###Standard template
该数组必须满足一下两点要求：
- 升序
- 没有重复的
```python
from typing import List


def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left >> 1)  # python 中 +-的运算级要高于移位，后面为了方便都这样写了
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

区分语法：

初始条件：left = 0, right = length-1<br/>
循环条件：left > right<br/>
向左查找：right = mid-1<br/>
向右查找：left = mid+1<br/>
该模板用于查找可以通过访问无重复数组中的单个索引来确定的元素或条件。<br/>
