"""
电话号码的字母组合

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""
from typing import List


def letter_combinations(digits: str) -> List[str]:
    mappings = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    n = len(digits)
    ans = []

    def combination(cs: List[str], k: int):
        if len(cs) == n:
            ans.append(''.join(cs))
        else:
            for i in range(k, n):
                digit = digits[i]
                if digit in mappings:
                    for c in mappings[digit]:
                        cs.append(c)
                        combination(cs, i + 1)
                        cs.pop()
    if n > 0:
        combination([], 0)
    return ans

if __name__ == '__main__':
    print(letter_combinations(''))
    print(letter_combinations('23'))