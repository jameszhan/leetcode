"""
最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

#### 示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


"""
思路和算法

假设 nums 数组的长度是 n，下标从 0 到 n−1。

我们用 ai 代表 nums[i]，用 f(i) 代表以第 i 个数结尾的「连续子数组的最大和」，那么很显然我们要求的答案就是：

max{f(i)}, 0≤i≤n−1

因此我们只需要求出每个位置的 f(i)，然后返回 f 数组中的最大值即可。那么我们如何求 f(i) 呢？我们可以考虑 ai 单独成为一段还是加入 f(i−1) 
对应的那一段，这取决于 ai 和 f(i−1)+ai 的大小，我们希望获得一个比较大的，于是可以写出这样的动态规划转移方程：

f(i) = max{f(i−1)+ai, ai}
"""


def max_sub_array(nums) -> int:
    nums_len = len(nums)
    if nums_len <= 0:
        return 0
    elif nums_len == 1:
        return nums[0]
    else:
        ans = -0x80000000
        pre = 0
        for i in range(nums_len):
            pre = max(nums[i], pre + nums[i])
            ans = max(ans, pre)
        return ans


if __name__ == '__main__':
    print(max_sub_array([1, 2]))
    print(max_sub_array([-8, -9, -7, -3, -5, -6]))
    print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_sub_array([-3, -2, 50, -1, -2, -6, 8, -3, 1, 7]))
    print(max_sub_array([50, -60, 30, -20, 10, 40, -50]))



