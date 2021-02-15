"""
接雨水 II

给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。

#### 示例：

给出如下 3x6 的高度图:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
返回 4 。


如上图所示，这是下雨前的高度图[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] 的状态。

下雨后，雨水将会被存储在这些方块中。总的接雨水量是4。

#### 提示：

1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000
"""


def trap_rain_water(height_map) -> int:
    def find_max_left(gm, i, j):
        max_left = gm[i][j][0]
        for k in range(j):
            max_left = max(gm[i][k][0], max_left)

        max_left_top = max_left_bottom = 20000
        if j > 1 and 1 < i < len(gm) - 2:
            max_left_top = find_max_top(gm, i, j - 1)
            max_left_bottom = find_max_bottom(gm, i, j - 1)
        return min(max_left, max_left_top, max_left_bottom)

    def find_max_right(gm, i, j):
        c_len = len(gm[i])
        max_right = gm[i][j][1]
        for k in range(j + 1, c_len):
            max_right = max(gm[i][k][1], max_right)

        max_right_top = max_right_bottom = 20000
        if j < c_len - 2:
            max_right_top = find_max_top(gm, i, j + 1)
            max_right_bottom = find_max_bottom(gm, i, j + 1)
        return min(max_right, max_right_top, max_right_bottom)

    def find_max_top(gm, i, j):
        max_top = gm[i][j][2]
        for k in range(i):
            max_top = max(gm[k][j][2], max_top)

        max_top_left = max_top_right = 20000
        if i > 1 and 1 < j < len(gm[i]) - 2:
            max_top_left = find_max_left(gm, i - 1, j)
            max_top_right = find_max_right(gm, i - 1, j)
        return min(max_top, max_top_left, max_top_right)

    def find_max_bottom(gm, i, j):
        r_len = len(gm)
        max_bottom = gm[i][j][3]
        for k in range(i + 1, r_len):
            max_bottom = max(gm[k][j][3], max_bottom)
        max_bottom_left = max_bottom_right = 20000
        if i < r_len - 2:
            max_bottom_left = find_max_left(gm, i + 1, j)
            max_bottom_right = find_max_right(gm, i + 1, j)
        return min(max_bottom, max_bottom_left, max_bottom_right)

    hm_len = len(height_map)
    if hm_len <= 1:
        return 0

    guard_map = []
    for i in range(hm_len):
        row = height_map[i]
        guard_map.append([[0, 0, 0, 0] for _ in row])  # left, right, top, bottom

    for i in range(hm_len):
        row = height_map[i]
        row_len = len(row)
        for j in range(row_len):
            if j > 0:
                guard_map[i][j][0] = height_map[i][j - 1]  # LEFT
            if j < row_len - 1:
                guard_map[i][j][1] = height_map[i][j + 1]  # RIGHT
            if i > 0:
                guard_map[i][j][2] = height_map[i - 1][j]  # TOP
            if i < hm_len - 1:
                guard_map[i][j][3] = height_map[i + 1][j]  # BOTTOM

    total = 0
    for i in range(hm_len):
        row = height_map[i]
        row_len = len(row)
        for j in range(row_len):
            # left, right, top, bottom = guard_map[i][j]
            left = find_max_left(guard_map, i, j)
            right = find_max_right(guard_map, i, j)
            top = find_max_top(guard_map, i, j)
            bottom = find_max_bottom(guard_map, i, j)
            height = height_map[i][j]
            # print(i, j, (left, right, top, bottom), height, min(left, right, top, bottom) - height)
            if height < left and height < right and height < top and height < bottom:
                total += min(left, right, top, bottom) - height
    return total


if __name__ == '__main__':
    print(trap_rain_water([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))
    print(trap_rain_water([[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]))
    print(trap_rain_water([[5, 5, 5, 1], [5, 1, 1, 5], [5, 1, 5, 5], [5, 2, 5, 8]]))
