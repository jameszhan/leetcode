"""
最小覆盖子串

给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""


def min_window(s: str, t: str) -> str:

    def contains(counter, target):
        for k in counter:
            if counter[k] < target[k]:
                return False
        return True

    if not s or not t:
        return ""

    target = {}
    for c in t:
        if c in target:
            target[c] += 1
        else:
            target[c] = 1

    m, n = len(s), len(t)
    if m < n:
        return ""

    counter = {}
    for c in t:
        counter[c] = 0

    ans = ''
    left = 0
    right = 0
    while right < m:
        ch = s[right]
        if ch in target:
            counter[ch] += 1
        while contains(counter, target):
            res = s[left:right+1]
            if len(ans) == 0 or len(res) < len(ans):
                ans = res

            c = s[left]
            if c in counter:
                counter[c] -= 1
            left += 1

        right += 1

    return ans


if __name__ == '__main__':
    print(min_window("ADOBECODEBANC", "ABC"))