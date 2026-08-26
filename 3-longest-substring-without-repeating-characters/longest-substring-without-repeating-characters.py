#adit

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start = 0
        max_len = 0
        for end, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= start:
                start = last_seen[ch]+1
            last_seen[ch] = end
            max_len = max(max_len, end - start + 1)
        return max_len
        