"""
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

示例:

输入: "Hello World"
输出: 5
"""


def length_of_last_word(s) -> int:
    s_len = len(s)
    if s_len <= 0:
        return 0
    i = s_len - 1
    while i >= 0 and s[i] == ' ':
        i -= 1

    ans = 0
    while i >= 0:
        if s[i] == ' ':
            break
        else:
            ans += 1
        i -= 1
    return ans


if __name__ == '__main__':
    print(length_of_last_word(""))
    print(length_of_last_word(" "))
    print(length_of_last_word("a"))
    print(length_of_last_word("a "))
    print(length_of_last_word("World    "))
    print(length_of_last_word(" World"))
    print(length_of_last_word("Hello World"))