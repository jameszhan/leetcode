"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

#### 示例 1:

输入: ["flower","flow","flight"]
输出: "fl"


#### 示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明: 所有输入只包含小写字母 a-z 。
"""


def longest_common_prefix(strs) -> str:
    strs_len = len(strs)
    if strs_len == 0:
        return ""
    elif strs_len == 1:
        return strs[0]
    else:
        l = min(map(len, strs))
        bs = strs[0]
        for i in range(l):
            prefix = bs[0:i+1]
            for j in range(1, strs_len):
                s = strs[j]
                if s[0:i+1] != prefix:
                    return s[0:i]
        return bs[0:l]


if __name__ == '__main__':
    print(longest_common_prefix(["flower", "flow", "flight"]))
    print(longest_common_prefix(["dog", "racecar", "car"]))
    print(longest_common_prefix(["a", "b"]))