"""
最长有效括号

给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"


示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""


def longest_valid_parentheses(s: str) -> int:
    if not s:
        return 0

    n, ans, stack = len(s), 0, [0]
    for i in range(1, n):
        c = s[i]
        if not stack or c == '(' or s[stack[-1]] == ')':
            stack.append(i)
        elif c == ')':
            stack.pop()
            if not stack:
                ans = max(ans, i + 1)
            else:
                ans = max(ans, i - stack[-1])
    return ans


if __name__ == '__main__':
    print(longest_valid_parentheses('(()'))
    print(longest_valid_parentheses(')()())'))
    print(longest_valid_parentheses('()(()'))
    print(longest_valid_parentheses('()((()))'))
    print(longest_valid_parentheses('())'))

