class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n
        center = right = 0

        for i in range(n):
            if i < right:
                p[i] = min(right - i, p[2 * center - i])
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1
            if i + p[i] > right:
                center, right = i, i + p[i]

        max_len, center_idx = max((v, i) for i, v in enumerate(p))
        start = (center_idx - max_len) // 2
        return s[start:start + max_len]