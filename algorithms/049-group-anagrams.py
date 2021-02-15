"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

#### 示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
"""


def group_anagrams(strs):
    d = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key in d:
            d[key].append(s)
        else:
            d[key] = [s]

    ans = []
    for k in d:
        ans.append(d[k])

    return ans


if __name__ == '__main__':
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))