from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        t_count = Counter(t)
        window_count = {}
        
        required = len(t_count)
        formed = 0
        
        l, r = 0, 0
        ans = (float('inf'), 0, 0)

        while r < len(s):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            while l <= r and formed == required:
                char = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]