"""
接雨水

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

#### 示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""


def trap(heights) -> int:
    total, length = 0, len(heights)
    if length <= 2:
        return 0
    max_left, max_right = [0 for _ in range(length)], [0 for _ in range(length)]
    # max_left[0] = heights[0]
    # max_right[length - 1] = heights[length - 1]

    for i in range(1, length):
        max_left[i] = max(max_left[i - 1], heights[i - 1])
    for i in reversed(range(0, length - 1)):
        max_right[i] = max(max_right[i + 1], heights[i + 1])

    for i in range(1, length - 1):
        m = min(max_left[i], max_right[i])
        if m > heights[i]:
            total += (m - heights[i])

    return total


if __name__ == '__main__':
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(trap([2, 5, 1, 2, 3, 4, 7, 2]))
    print(trap([2, 0, 2]))
    print(trap([2, 5]))
    print(trap([]))
