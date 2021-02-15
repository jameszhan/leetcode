"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。


#### 示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。


#### 示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。


#### 示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。


#### 示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".


#### 示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false
"""


def is_match(s: str, p: str) -> bool:
    sn, pn = len(s), len(p)
    i, j = 0, 0
    k, star = 0, -1  #  处理 '*' 场景
    while i < sn:
        if j < pn and (s[i] == p[j] or p[j] == '?'):
            i += 1
            j += 1
        elif j < pn and p[j] == '*':
            k = i
            star = j
            j += 1
        elif star != -1:
            j = star + 1
            k += 1
            i = k
        else:
            return False
    if j < pn:
        while j < pn:
            if p[j] != '*':
                return False
            j += 1
    return True


if __name__ == '__main__':
    print(is_match("aa", "a"))
    print(is_match("aa", "*"))
    print(is_match("cb", "?a"))
    print(is_match("adceb", "*a*b"))
    print(is_match("acdcb", "a*c?b"))