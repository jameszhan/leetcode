"""
三数之和

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

#### 示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def three_sum(nums):
    length = len(nums)
    ans = []
    if length < 3:
        return ans

    nums.sort()
    already_processed = set()

    for i in range(length):
        if nums[i] > 0:
            break

        if nums[i] in already_processed:
            continue

        this_round = []
        left, right = i + 1, length - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                a = [nums[i], nums[left], nums[right]]
                already_processed.add(nums[i])

                if a not in this_round:
                    this_round.append(a)
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            elif s > 0:
                right -= 1
        ans.extend(this_round)
    return ans


if __name__ == '__main__':
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(three_sum([0, 0, 0, 0]))
    print(three_sum([-2, 0, 0, 2, 2]))
    print(three_sum([3, 0, -2, -1, 1, 2]))
