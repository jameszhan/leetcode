"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

#### 示例 1:

输入: "()"
输出: true


#### 示例 2:

输入: "()[]{}"
输出: true


#### 示例 3:

输入: "(]"
输出: false


#### 示例 4:

输入: "([)]"
输出: false


#### 示例 5:

输入: "{[]}"
输出: true
"""


def is_valid(s: str) -> bool:
    stack = []
    for c in s:
        if len(stack) == 0:
            if c == ')' or c == ']' or c == '}':
                return False
            else:
                stack.append(c)
        else:
            if c == ')' and stack[-1] == '(' or c == ']' and stack[-1] == '[' or c == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(c)
    return len(stack) == 0


if __name__ == '__main__':
    print(is_valid("()"))
    print(is_valid("()[]{}"))
    print(is_valid("(]"))
    print(is_valid("([)]"))
    print(is_valid("{[]}"))