"""
无重复字符的最长子串

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。


示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


def length_of_longest_substring(s: str) -> int:
    if not s:
        return 0
    max_len = 0
    c_list = []
    curr_len = 0
    for i in range(len(s)):
        curr_len += 1
        c = s[i]
        # while c in c_list:
        #     del c_list[0]
        #     curr_len -= 1
        if c in c_list:
            pos = c_list.index(c)
            del c_list[0:pos+1]
            curr_len -= (pos + 1)

        c_list.append(c)
        max_len = max(curr_len, max_len)
    return max_len


if __name__ == '__main__':
    print(length_of_longest_substring("abcabcbb"))
    print(length_of_longest_substring("bbbbb"))
    print(length_of_longest_substring("pwwkew"))


