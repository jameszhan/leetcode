"""
除自身以外数组的乘积

给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

#### 示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
 
提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

#### 进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
"""


# def product_except_self(nums):
#     nl = len(nums)
#     output = []
#     for i in range(nl):
#         product = 1
#         for j, num in enumerate(nums):
#             if j != i:
#                 product *= num
#         output.append(product)
#     return output

def product_except_self(nums):
    nl = len(nums)
    left, right = 1, 1
    output = [1 for _ in range(nl)]
    for i in range(nl):
        output[i] = left
        left *= nums[i]

    for i in reversed(range(nl)):
        output[i] *= right
        right *= nums[i]
    return output


if __name__ == '__main__':
    print(product_except_self([9, 8, 7]))
    print(product_except_self([1, 2, 3, 4]))
    print(product_except_self([5, 6, 7, 8]))

